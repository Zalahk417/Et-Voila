import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class BVPIngressContractTests(unittest.TestCase):
    def test_cloudflare_generates_and_propagates_trace_keys(self):
        js = (ROOT / "website" / "functions" / "api" / "enquiry.js").read_text(encoding="utf-8")
        self.assertIn("crypto.randomUUID()", js)
        self.assertIn('crypto.subtle.digest("SHA-256"', js)
        self.assertIn('"x-bvp-correlation-id"', js)
        self.assertIn('"x-bvp-idempotency-key"', js)
        self.assertIn("payload.correlation_id", js)
        self.assertIn("payload.idempotency_key", js)

    def test_n8n_preserves_keys_and_keeps_stage1_no_write(self):
        wf = json.loads((ROOT / "n8n" / "voila-floor-lead-intake-stage1.json").read_text(encoding="utf-8"))
        self.assertFalse(wf["active"])
        code = next(n for n in wf["nodes"] if n["name"] == "Normalise + Safety Gate")["parameters"]["jsCode"]
        self.assertIn("correlation_id", code)
        self.assertIn("idempotency_key", code)
        self.assertIn("BVP correlation ID:", code)
        self.assertIn("DRY_RUN_NO_WRITES", code)
        self.assertNotIn("api.servicem8.com", code)

if __name__ == "__main__":
    unittest.main()
