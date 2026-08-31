from __future__ import annotations

import hashlib
import json
import re
from typing import Any

from .models import Lead, LeadDecision

SERVICE_ALIASES = {
    "carpet": "carpet_cleaning",
    "carpet cleaning": "carpet_cleaning",
    "upholstery": "upholstery_cleaning",
    "couch": "upholstery_cleaning",
    "sofa": "upholstery_cleaning",
    "tile": "tile_grout",
    "grout": "tile_grout",
    "tile and grout": "tile_grout",
    "tile & grout": "tile_grout",
    "vinyl": "hard_floor",
    "stone": "hard_floor",
    "concrete": "hard_floor",
    "hard floor": "hard_floor",
    "stripping": "hard_floor_restoration",
    "sealing": "hard_floor_restoration",
    "restoration": "restoration_review",
    "water damage": "restoration_review",
}

HIGH_RISK_PATTERNS = {
    "water_or_flood": r"\b(flood|flooded|water damage|sewage|black water|burst pipe)\b",
    "mould_or_contamination": r"\b(mould|mold|biohazard|blood|faec|feces|needle|contamination)\b",
    "guarantee_request": r"\b(guarantee|100%|definitely remove|promise.*remove)\b",
    "insurance_or_liability": r"\b(insurance claim|liability|compensation|damages claim)\b",
    "urgent_health_safety": r"\b(asbestos|chemical spill|hazardous|toxic)\b",
}

def _clean(value: Any) -> str:
    if value is None:
        return ""
    return " ".join(str(value).strip().split())

def _normalise_service(raw_service: str, message: str) -> str:
    text = f"{raw_service} {message}".lower()
    for alias, canonical in sorted(SERVICE_ALIASES.items(), key=lambda kv: len(kv[0]), reverse=True):
        if alias in text:
            return canonical
    return "unknown"

def normalise_payload(payload: dict[str, Any]) -> Lead:
    name = _clean(payload.get("customer_name") or payload.get("name"))
    email = _clean(payload.get("email"))
    phone = _clean(payload.get("phone") or payload.get("mobile"))
    address = _clean(payload.get("job_address") or payload.get("address") or payload.get("site_address"))
    suburb = _clean(payload.get("suburb") or payload.get("city"))
    postcode = _clean(payload.get("postcode"))
    message = _clean(payload.get("message") or payload.get("enquiry") or payload.get("description"))
    raw_service = _clean(payload.get("service"))
    service = _normalise_service(raw_service, message)
    customer_type = _clean(payload.get("customer_type") or "unknown").lower()
    source = _clean(payload.get("source") or "unknown").lower()
    measurements = _clean(payload.get("measurements") or payload.get("area"))
    preferred_timing = _clean(payload.get("preferred_timing") or payload.get("date_requested"))
    attachments_present = bool(payload.get("attachments_present") or payload.get("attachments"))
    known = {"source","customer_name","name","email","phone","mobile","job_address","address","site_address","suburb","city","postcode","message","enquiry","description","service","customer_type","measurements","area","preferred_timing","date_requested","attachments_present","attachments"}
    metadata = {k: v for k, v in payload.items() if k not in known}
    return Lead(source=source, customer_name=name, email=email, phone=phone, job_address=address, suburb=suburb, postcode=postcode, customer_type=customer_type, service=service, message=message, measurements=measurements, preferred_timing=preferred_timing, attachments_present=attachments_present, metadata=metadata)

def required_missing_fields(lead: Lead) -> list[str]:
    missing: list[str] = []
    if not lead.customer_name: missing.append("customer_name")
    if not (lead.email or lead.phone): missing.append("contact_method")
    if not (lead.job_address or (lead.suburb and lead.postcode)): missing.append("job_location")
    if lead.service == "unknown": missing.append("service")
    return missing

def risk_flags(lead: Lead) -> list[str]:
    text = f"{lead.service} {lead.message}".lower()
    flags = [name for name, pattern in HIGH_RISK_PATTERNS.items() if re.search(pattern, text, re.I)]
    if lead.service == "restoration_review" or any(x in flags for x in ["water_or_flood", "mould_or_contamination", "urgent_health_safety"]):
        flags.append("restoration_requires_review")
    return sorted(set(flags))

def make_idempotency_key(lead: Lead) -> str:
    canonical = {"name": lead.customer_name.lower(), "email": lead.email.lower(), "phone": re.sub(r"\D", "", lead.phone), "address": lead.job_address.lower(), "suburb": lead.suburb.lower(), "postcode": lead.postcode, "service": lead.service, "message": lead.message.lower(), "source": lead.source}
    raw = json.dumps(canonical, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:24]

def build_servicem8_job_draft(lead: Lead) -> dict[str, Any]:
    location = lead.job_address or ", ".join(x for x in [lead.suburb, lead.postcode] if x)
    lines = [f"Voila Floor lead source: {lead.source}", f"Service: {lead.service}"]
    if lead.measurements: lines.append(f"Measurements/items stated: {lead.measurements}")
    if lead.preferred_timing: lines.append(f"Preferred timing: {lead.preferred_timing}")
    if lead.message: lines.append(f"Customer enquiry: {lead.message}")
    lines.append("AI/automation status: DRAFT ONLY — scope and price require human review.")
    return {"status": "Quote", "job_address": location, "job_description": "\n".join(lines)}

def decide(payload: dict[str, Any]) -> LeadDecision:
    lead = normalise_payload(payload)
    missing = required_missing_fields(lead)
    flags = risk_flags(lead)
    review = bool(missing or flags)
    return LeadDecision(lead=lead, missing_fields=missing, risk_flags=flags, human_review_required=review, safe_acknowledgement_allowed=not flags, idempotency_key=make_idempotency_key(lead), servicem8_job_draft=build_servicem8_job_draft(lead))
