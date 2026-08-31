from __future__ import annotations
import json, os, urllib.error, urllib.request
from pathlib import Path
from typing import Any
RESPONSES_URL = "https://api.openai.com/v1/responses"
class OpenAIExtractionError(RuntimeError): pass

def _load_schema(schema_path: str | None = None) -> dict[str, Any]:
    if schema_path: return json.loads(Path(schema_path).read_text(encoding="utf-8"))
    repo_schema = Path(__file__).resolve().parents[2] / "schemas" / "enquiry.schema.json"
    return json.loads(repo_schema.read_text(encoding="utf-8"))

def extract_output_text(response: dict[str, Any]) -> str:
    for item in response.get("output", []):
        if item.get("type") != "message": continue
        for content in item.get("content", []):
            if content.get("type") == "output_text" and isinstance(content.get("text"), str): return content["text"]
    raise OpenAIExtractionError("Responses API result contained no output_text")

def extract_enquiry_with_ai(raw_enquiry: str, schema_path: str | None = None) -> dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key: raise OpenAIExtractionError("OPENAI_API_KEY is not configured")
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    schema = _load_schema(schema_path)
    instruction = "Extract only explicitly stated facts from this Voila Floor Cleaning & Restoration enquiry. Never invent price, availability, measurements, surface type, stain outcomes, safety diagnosis or guarantees. Unknown values must remain empty/unknown. Flag water/flood/sewage, mould/contamination, asbestos/hazardous material, insurance/liability and guarantee requests. Return the required JSON schema only."
    payload = {"model": model, "store": False, "input": [{"role":"system","content":instruction},{"role":"user","content":raw_enquiry}], "text":{"format":{"type":"json_schema","name":"voila_floor_enquiry","description":"Structured extraction for a floor-care service enquiry","strict":True,"schema":schema}}}
    req = urllib.request.Request(RESPONSES_URL, data=json.dumps(payload).encode("utf-8"), method="POST", headers={"Authorization":f"Bearer {api_key}","Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp: result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace"); raise OpenAIExtractionError(f"OpenAI HTTP {exc.code}: {body[:500]}") from exc
    except urllib.error.URLError as exc: raise OpenAIExtractionError(f"OpenAI connection failed: {exc}") from exc
    try: return json.loads(extract_output_text(result))
    except json.JSONDecodeError as exc: raise OpenAIExtractionError("Structured output was not valid JSON") from exc
