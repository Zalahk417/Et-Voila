# Et-Voila — Voila Floor AI Automation

Production-minded automation foundation for **Voila Floor Cleaning & Restoration** (Midwest Trade Hub Pty Ltd).

## Current deployable slice

`Lead enquiry -> deterministic normalisation -> risk/missing-field gate -> optional AI structured extraction -> ServiceM8-ready draft -> human approval`

The repository defaults to **dry-run**. It will not create ServiceM8 jobs unless `VOILA_ALLOW_SERVICEM8_WRITES=true` is set intentionally.

## Design rules

- ServiceM8 remains the operational system of record.
- Native ServiceM8 automations are preferred over custom duplication.
- AI may extract/classify/draft; deterministic rules own pricing, safety gates and required fields.
- No autonomous pricing commitments, guarantees, refunds, complaint resolutions or restoration-risk decisions.
- Jim's/franchise-controlled historical data is excluded unless explicitly cleared for migration/use.
- Credentials live only in environment/secrets stores, never in prompts or committed files.

## Quick start

```bash
export PYTHONPATH=src
python -m unittest discover -s tests -v
python -m voila_floor.cli --input tests/fixtures_domestic_carpet.json
```

See `docs/DEPLOYMENT.md` for ServiceM8 and n8n setup.