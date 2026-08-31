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

    def _assert_write_enabled(self) -> None:
        if not self.allow_writes:
            raise ServiceM8Error("ServiceM8 write blocked: set VOILA_ALLOW_SERVICEM8_WRITES=true only after staging tests and owner approval")
