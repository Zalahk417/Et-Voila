from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

BASE_URL = "https://api.servicem8.com/api_1.0"

class ServiceM8Error(RuntimeError):
    pass

class ServiceM8Client:
    def __init__(self, api_key: str | None = None, allow_writes: bool | None = None):
        self.api_key = api_key or os.getenv("SERVICEM8_API_KEY", "")
        if allow_writes is None:
            allow_writes = os.getenv("VOILA_ALLOW_SERVICEM8_WRITES", "false").lower() == "true"
        self.allow_writes = allow_writes

    def _request(self, method: str, path: str, payload: dict[str, Any] | None = None):
        if not self.api_key:
            raise ServiceM8Error("SERVICEM8_API_KEY is not configured")
        url = f"{BASE_URL}/{path.lstrip('/')}"
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url=url, data=data, method=method)
        req.add_header("X-API-Key", self.api_key)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                body = resp.read().decode("utf-8").strip()
                parsed = json.loads(body) if body else None
                return parsed, {k.lower(): v for k, v in resp.headers.items()}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise ServiceM8Error(f"ServiceM8 HTTP {exc.code}: {body[:500]}") from exc
        except urllib.error.URLError as exc:
            raise ServiceM8Error(f"ServiceM8 connection failed: {exc}") from exc

    def get_company(self, uuid: str) -> dict[str, Any]:
        data, _ = self._request("GET", f"company/{urllib.parse.quote(uuid)}.json")
        if not isinstance(data, dict): raise ServiceM8Error("Unexpected company response")
        return data


    def get_job(self, uuid: str) -> dict[str, Any]:
        data, _ = self._request("GET", f"job/{urllib.parse.quote(uuid)}.json")
        if not isinstance(data, dict):
            raise ServiceM8Error("Unexpected job response")
        return data

    def search_jobs(self, query: str, limit: int = 50) -> list[dict[str, Any]]:
        query = query.strip()
        if not query:
            raise ServiceM8Error("Search query is required")
        if len(query) > 100:
            raise ServiceM8Error("Search query must be 100 characters or fewer")
        if not 1 <= limit <= 100:
            raise ServiceM8Error("Search limit must be between 1 and 100")
        params = urllib.parse.urlencode({"q": query, "limit": limit})
        data, _ = self._request("GET", f"search/job.json?{params}")
        if isinstance(data, list):
            return [item for item in data if isinstance(item, dict)]
        if isinstance(data, dict):
            for key in ("results", "data"):
                value = data.get(key)
                if isinstance(value, list):
                    return [item for item in value if isinstance(item, dict)]
        raise ServiceM8Error("Unexpected job search response")

    def create_job_from_template(
        self,
        template_uuid: str,
        *,
        company_name: str,
        job_address: str,
        job_description: str,
    ) -> str:
        self._assert_write_enabled()
        payload = {
            "company_name": company_name,
            "job_address": job_address,
            "job_description": job_description,
        }
        _, headers = self._request(
            "POST",
            f"jobtemplate/{urllib.parse.quote(template_uuid)}/job.json",
            payload,
        )
        uuid = headers.get("x-record-uuid", "")
        if not uuid:
            raise ServiceM8Error(
                "ServiceM8 did not return x-record-uuid for template job creation"
            )
        return uuid

    def create_company(self, name: str, address: str = "") -> str:
        self._assert_write_enabled()
        _, headers = self._request("POST", "company.json", {"name": name, "address": address})
        uuid = headers.get("x-record-uuid", "")
        if not uuid: raise ServiceM8Error("ServiceM8 did not return x-record-uuid for company creation")
        return uuid

    def create_job(self, company_uuid: str, job_draft: dict[str, Any]) -> str:
        self._assert_write_enabled()
        payload = dict(job_draft); payload["company_uuid"] = company_uuid; payload.setdefault("status", "Quote")
        _, headers = self._request("POST", "job.json", payload)
        uuid = headers.get("x-record-uuid", "")
        if not uuid: raise ServiceM8Error("ServiceM8 did not return x-record-uuid for job creation")
        return uuid

    # Documented ServiceM8 REST resources used by the backend admin bridge.
    # Keep this allowlist explicit: arbitrary paths are intentionally not exposed.
    ADMIN_RESOURCES = {
        "queue": "queue",
        "badge": "badge",
        "category": "category",
        "material": "material",
        "form": "form",
        "formfield": "formfield",
        "documenttemplate": "documenttemplate",
    }

    def list_records(self, resource: str) -> list[dict[str, Any]]:
        endpoint = self._admin_endpoint(resource)
        data, _ = self._request("GET", f"{endpoint}.json")
        if isinstance(data, list):
            return [item for item in data if isinstance(item, dict)]
        if isinstance(data, dict):
            for key in ("data", "results"):
                value = data.get(key)
                if isinstance(value, list):
                    return [item for item in value if isinstance(item, dict)]
        raise ServiceM8Error(f"Unexpected {resource} list response")

    def create_record(self, resource: str, payload: dict[str, Any]) -> str:
        self._assert_write_enabled()
        endpoint = self._admin_endpoint(resource)
        _, headers = self._request("POST", f"{endpoint}.json", payload)
        uuid = headers.get("x-record-uuid", "")
        if not uuid:
            raise ServiceM8Error(f"ServiceM8 did not return x-record-uuid for {resource} creation")
        return uuid

    def update_record(self, resource: str, uuid: str, payload: dict[str, Any]) -> None:
        self._assert_write_enabled()
        endpoint = self._admin_endpoint(resource)
        self._request("POST", f"{endpoint}/{urllib.parse.quote(uuid)}.json", payload)

    def delete_record(self, resource: str, uuid: str) -> None:
        self._assert_write_enabled()
        endpoint = self._admin_endpoint(resource)
        self._request("DELETE", f"{endpoint}/{urllib.parse.quote(uuid)}.json")

    def ensure_named_record(
        self,
        resource: str,
        name: str,
        payload: dict[str, Any] | None = None,
    ) -> tuple[str, bool]:
        """Return (uuid, created). Create only when no exact-name record exists."""
        wanted = name.strip()
        if not wanted:
            raise ServiceM8Error("Record name is required")
        matches = [
            row for row in self.list_records(resource)
            if str(row.get("name", "")).strip() == wanted
        ]
        if len(matches) > 1:
            raise ServiceM8Error(f"Duplicate {resource} records already exist for exact name: {wanted}")
        if matches:
            uuid = str(matches[0].get("uuid", "")).strip()
            if not uuid:
                raise ServiceM8Error(f"Existing {resource} record has no uuid: {wanted}")
            return uuid, False
        body = dict(payload or {})
        body["name"] = wanted
        uuid = self.create_record(resource, body)
        reread = [
            row for row in self.list_records(resource)
            if str(row.get("name", "")).strip() == wanted
        ]
        if len(reread) != 1 or str(reread[0].get("uuid", "")).strip() != uuid:
            raise ServiceM8Error(f"Read-back verification failed for {resource}: {wanted}")
        return uuid, True

    def _admin_endpoint(self, resource: str) -> str:
        try:
            return self.ADMIN_RESOURCES[resource]
        except KeyError as exc:
            raise ServiceM8Error(f"Unsupported admin resource: {resource}") from exc

    def _assert_write_enabled(self) -> None:
        if not self.allow_writes:
            raise ServiceM8Error("ServiceM8 write blocked: set VOILA_ALLOW_SERVICEM8_WRITES=true only after staging tests and owner approval")
