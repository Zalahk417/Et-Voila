#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

BASE = "https://api.servicem8.com/api_1.0"
MANIFEST = Path("config/servicem8.bootstrap.manifest.json")
EVIDENCE = Path("servicem8-bootstrap-evidence.json")


class SM8Error(RuntimeError):
    pass


def request(method: str, path: str, payload=None):
    key = os.environ.get("SERVICEM8_API_KEY", "").strip()
    if not key:
        raise SM8Error("SERVICEM8_API_KEY is not available to this runtime")
    url = f"{BASE}/{path.lstrip('/')}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    for attempt in range(5):
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("X-API-Key", key)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8").strip()
                body = json.loads(raw) if raw else None
                headers = {k.lower(): v for k, v in resp.headers.items()}
                return body, headers
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            if exc.code == 429 and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise SM8Error(f"{method} {path} -> HTTP {exc.code}: {raw[:1200]}") from exc
        except urllib.error.URLError as exc:
            if attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise SM8Error(f"{method} {path} connection failed: {exc}") from exc
    raise SM8Error(f"{method} {path} failed after retries")


def get_list(path: str):
    body, _ = request("GET", path)
    if not isinstance(body, list):
        raise SM8Error(f"Unexpected list response from {path}: {type(body).__name__}")
    return body


def create(path: str, payload: dict):
    _, headers = request("POST", path, payload)
    return headers.get("x-record-uuid", "")


def active(records):
    return [r for r in records if str(r.get("active", "1")) != "0"]


def exact_name_counts(records):
    return Counter((r.get("name") or "").strip() for r in active(records))


def archive_record(endpoint: str, uuid: str) -> None:
    resource = endpoint[:-5] if endpoint.endswith(".json") else endpoint
    request("DELETE", f"{resource}/{uuid}.json")


def dedupe_named(endpoint: str, desired: list[str]):
    rows = active(get_list(endpoint))
    archived = []
    kept = []
    for name in desired:
        matches = sorted(
            [r for r in rows if (r.get("name") or "").strip() == name],
            key=lambda r: (r.get("uuid") or ""),
        )
        if not matches:
            continue
        keeper = matches[0]
        kept.append({"name": name, "uuid": keeper.get("uuid")})
        for extra in matches[1:]:
            uuid = extra.get("uuid") or ""
            if uuid:
                archive_record(endpoint, uuid)
                archived.append({"name": name, "uuid": uuid})
    return {"kept": kept, "archived": archived}


def dedupe_materials(items: list[dict]):
    desired_codes = {item["item_number"] for item in items}
    rows = active(get_list("material.json"))
    groups = {}
    for r in rows:
        code = (r.get("item_number") or "").strip()
        if code in desired_codes:
            groups.setdefault(code, []).append(r)
    archived = []
    kept = []
    for code, matches in groups.items():
        matches = sorted(matches, key=lambda r: (r.get("uuid") or ""))
        keeper = matches[0]
        kept.append({"item_number": code, "name": keeper.get("name"), "uuid": keeper.get("uuid")})
        for extra in matches[1:]:
            uuid = extra.get("uuid") or ""
            if uuid:
                archive_record("material.json", uuid)
                archived.append({"item_number": code, "name": extra.get("name"), "uuid": uuid})
    return {"kept": kept, "archived": archived}


def ensure_gst_rate():
    tax_rates = active(get_list("taxrate.json"))
    matches = [
        r for r in tax_rates
        if (r.get("name") or "").upper() == "GST"
        and float(r.get("amount") or 0) == 10.0
    ]
    created = False
    archived = []
    if not matches:
        gst_uuid = create("taxrate.json", {"name": "GST", "amount": "10", "is_default_tax_rate": 0})
        tax_rates = active(get_list("taxrate.json"))
        matches = [
            r for r in tax_rates
            if (r.get("uuid") or "") == gst_uuid
            or ((r.get("name") or "").upper() == "GST" and float(r.get("amount") or 0) == 10.0)
        ]
        created = True
    if not matches:
        raise SM8Error("Unable to establish a 10% GST tax rate; refusing to create catalogue")

    matches = sorted(
        matches,
        key=lambda r: (
            0 if str(r.get("is_default_tax_rate", "0")) == "1" else 1,
            r.get("uuid") or "",
        ),
    )
    gst = matches[0]
    for extra in matches[1:]:
        uuid = extra.get("uuid") or ""
        if uuid:
            archive_record("taxrate.json", uuid)
            archived.append({"name": extra.get("name"), "amount": extra.get("amount"), "uuid": uuid})
    return gst, created, archived


def ensure_named(endpoint: str, desired: list[str], extra=None):
    rows = get_list(endpoint)
    counts = exact_name_counts(rows)
    created = []
    existing = []
    for name in desired:
        if counts.get(name, 0) >= 1:
            existing.append(name)
            continue
        payload = {"name": name}
        if extra:
            payload.update(extra(name))
        uuid = create(endpoint, payload)
        created.append({"name": name, "uuid": uuid})
        counts[name] += 1
    return {"created": created, "existing": existing, "duplicates": {k:v for k,v in counts.items() if k in desired and v > 1}}


def material_payload(item: dict, gst_uuid: str):
    payload = {
        "name": item["name"],
        "item_number": item["item_number"],
        "price_includes_taxes": 0,
        "item_is_inventoried": 1 if item.get("inventory_treatment") == "Tracked via accounting" else 0,
        "tax_rate_uuid": gst_uuid,
    }
    if item.get("cost_ex_gst") is not None:
        payload["cost"] = str(item["cost_ex_gst"])
    if item.get("sell_price_ex_gst") is not None:
        payload["price"] = str(item["sell_price_ex_gst"])
    desc_bits = ["Voilà"]
    if item.get("catalogue_type"):
        desc_bits.append(item["catalogue_type"])
    if item.get("supplier"):
        desc_bits.append(item["supplier"])
    if item.get("pack_size") is not None and item.get("pack_uom"):
        desc_bits.append(f'{item["pack_size"]} {item["pack_uom"]}')
    if item.get("service_family"):
        desc_bits.append(str(item["service_family"]))
    note = (item.get("notes") or "").strip()
    if note:
        desc_bits.append(note)
    payload["item_description"] = " | ".join(desc_bits)[:1800]
    return payload


def ensure_materials(items: list[dict], gst_uuid: str):
    rows = active(get_list("material.json"))
    by_number = {}
    by_name = {}
    duplicate_item_numbers = {}
    duplicate_names = {}
    for r in rows:
        n = (r.get("item_number") or "").strip()
        name = (r.get("name") or "").strip()
        if n:
            if n in by_number:
                duplicate_item_numbers[n] = duplicate_item_numbers.get(n, 1) + 1
            else:
                by_number[n] = r
        if name:
            if name in by_name:
                duplicate_names[name] = duplicate_names.get(name, 1) + 1
            else:
                by_name[name] = r

    created = []
    existing = []
    conflicts = []
    for item in items:
        code = item["item_number"]
        name = item["name"]
        hit = by_number.get(code)
        if hit:
            existing.append({"name": name, "item_number": code, "uuid": hit.get("uuid")})
            continue
        name_hit = by_name.get(name)
        if name_hit:
            existing.append({"name": name, "item_number": name_hit.get("item_number"), "uuid": name_hit.get("uuid"), "matched_by": "name"})
            continue
        try:
            uuid = create("material.json", material_payload(item, gst_uuid))
            created.append({"name": name, "item_number": code, "uuid": uuid})
            by_number[code] = {"uuid": uuid, "name": name, "item_number": code}
            by_name[name] = by_number[code]
        except SM8Error as exc:
            conflicts.append({"name": name, "item_number": code, "error": str(exc)})
    return {
        "created": created,
        "existing": existing,
        "conflicts": conflicts,
        "duplicate_item_numbers": duplicate_item_numbers,
        "duplicate_names": duplicate_names,
    }


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    # Authentication + target read probe.
    staff = get_list("staff.json")
    if not staff:
        raise SM8Error("Authenticated tenant returned no staff; refusing bootstrap")

    # Repair duplicate records left by any earlier concurrent bootstrap runs.
    # All cleanup is scoped to the approved Voilà manifest and uses ServiceM8
    # soft-delete semantics, so archived duplicates remain recoverable.
    duplicate_cleanup = {
        "categories": dedupe_named("category.json", manifest["categories"]),
        "queues": dedupe_named("queue.json", manifest["queues"]),
        "badges": dedupe_named("badge.json", manifest["badges"]),
        "materials": dedupe_materials(manifest["materials"]),
    }
    gst, gst_created, gst_archived = ensure_gst_rate()
    duplicate_cleanup["gst"] = {"archived": gst_archived}

    # Safe bootstrap writes: create anything from the approved manifest that is
    # still missing after cleanup.
    categories = ensure_named("category.json", manifest["categories"])
    queues = ensure_named("queue.json", manifest["queues"], lambda _n: {"requires_assignment": 0, "default_timeframe": 0})
    badges = ensure_named("badge.json", manifest["badges"])
    materials = ensure_materials(manifest["materials"], gst["uuid"])

    # Independent read-back.
    readback = {
        "categories": exact_name_counts(get_list("category.json")),
        "queues": exact_name_counts(get_list("queue.json")),
        "badges": exact_name_counts(get_list("badge.json")),
        "material_count": len(active(get_list("material.json"))),
    }
    missing_categories = [n for n in manifest["categories"] if readback["categories"].get(n, 0) < 1]
    missing_queues = [n for n in manifest["queues"] if readback["queues"].get(n, 0) < 1]
    missing_badges = [n for n in manifest["badges"] if readback["badges"].get(n, 0) < 1]

    evidence = {
        "schema_version": 1,
        "project": "voila-floor-care",
        "target": "ServiceM8 clean Voilà tenant",
        "manifest_items": len(manifest["materials"]),
        "tax_rate": {
            "name": gst.get("name"),
            "amount": gst.get("amount"),
            "uuid": gst.get("uuid"),
            "created": gst_created,
            "is_default_tax_rate": gst.get("is_default_tax_rate"),
        },
        "duplicate_cleanup": duplicate_cleanup,
        "result": {
            "categories": categories,
            "queues": queues,
            "badges": badges,
            "materials": materials,
        },
        "readback": {
            "missing_categories": missing_categories,
            "missing_queues": missing_queues,
            "missing_badges": missing_badges,
            "material_count": readback["material_count"],
            "queue_duplicate_counts": {n:c for n,c in readback["queues"].items() if n in manifest["queues"] and c > 1},
            "badge_duplicate_counts": {n:c for n,c in readback["badges"].items() if n in manifest["badges"] and c > 1},
        },
    }

    hard_fail = bool(missing_categories or missing_queues or missing_badges or materials["conflicts"])
    evidence["outcome"] = "FAIL" if hard_fail else ("PASS_WITH_DUPLICATE_WARNING" if evidence["readback"]["queue_duplicate_counts"] or evidence["readback"]["badge_duplicate_counts"] else "PASS")
    EVIDENCE.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2, ensure_ascii=False))

    if hard_fail:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
