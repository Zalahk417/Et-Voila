import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from voila_floor.audit import log_decision
from voila_floor.lead_intake import decide
from voila_floor.servicem8 import ServiceM8Client, ServiceM8Error

class LeadIntakeTests(unittest.TestCase):
    def test_normal_domestic_lead(self):
        d=decide({"source":"website","customer_name":"Alex Example","email":"alex@example.invalid","job_address":"12 Example Street, Geraldton WA 6530","service":"carpet cleaning","message":"Three bedrooms and a lounge with pet stains."})
        self.assertEqual(d.lead.service,"carpet_cleaning"); self.assertEqual(d.missing_fields,[]); self.assertEqual(d.risk_flags,[]); self.assertFalse(d.human_review_required); self.assertEqual(d.servicem8_job_draft["status"],"Quote")
    def test_high_risk_restoration_forces_review(self):
        d=decide({"customer_name":"Casey Example","phone":"0400 000 000","suburb":"Geraldton","postcode":"6530","message":"Office flooded after burst pipe, possible mould. Can you guarantee removal?"})
        self.assertTrue(d.human_review_required); self.assertIn("water_or_flood",d.risk_flags); self.assertIn("mould_or_contamination",d.risk_flags); self.assertIn("guarantee_request",d.risk_flags); self.assertIn("restoration_requires_review",d.risk_flags)
    def test_missing_contact_forces_review(self):
        d=decide({"customer_name":"No Contact","job_address":"Geraldton WA","service":"tile and grout","message":"Kitchen and hallway"})
        self.assertIn("contact_method",d.missing_fields); self.assertTrue(d.human_review_required)
    def test_idempotency_is_stable(self):
        p={"source":"website","customer_name":"A","email":"a@example.invalid","job_address":"1 Test St","service":"carpet","message":"2 rooms"}; self.assertEqual(decide(p).idempotency_key,decide(p).idempotency_key)
    def test_duplicate_audit_not_reinserted(self):
        d=decide({"source":"website","customer_name":"A","email":"a@example.invalid","job_address":"1 Test St","service":"carpet","message":"2 rooms"}).to_dict()
        with tempfile.TemporaryDirectory() as td:
            path=os.path.join(td,"audit.sqlite3"); self.assertTrue(log_decision(d,path)); self.assertFalse(log_decision(d,path))
    def test_servicem8_writes_are_blocked_by_default(self):
        c=ServiceM8Client(api_key="fake",allow_writes=False)
        with self.assertRaises(ServiceM8Error): c.create_job("00000000-0000-0000-0000-000000000000",{"status":"Quote"})

class OpenAIResponseParsingTests(unittest.TestCase):
    def test_extract_output_text(self):
        from voila_floor.openai_extract import extract_output_text
        fake={"output":[{"type":"message","content":[{"type":"output_text","text":"{\"ok\": true}"}]}]}; self.assertEqual(extract_output_text(fake),'{"ok": true}')

if __name__ == "__main__": unittest.main()
