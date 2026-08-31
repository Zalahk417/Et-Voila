# n8n Blueprint — Voila Floor Lead Intake

1. Trigger — website webhook/email/lead source.
2. Normalise to canonical enquiry shape.
3. Calculate replay/idempotency key.
4. Deduplicate.
5. AI structured extraction using `schemas/enquiry.schema.json` with no write authority.
6. Deterministic validation independent of model output.
7. Human-review branch for missing/risky/ambiguous cases.
8. Read-only ServiceM8 client lookup.
9. Human approval during staging/early production.
10. Create/update client only after dedupe.
11. Create ServiceM8 job with `status=Quote` and draft label.
12. Audit log.
13. Acknowledgement draft.
14. Error workflow for 401/403/429/5xx with safe retry rules.

Always human: price/scope commitments, restoration hazards, guarantees, complaints/insurance/liability, low-confidence extraction and initial production writes.
