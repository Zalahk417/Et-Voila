# Et-Voila — Voilà Floor Care automation

Production-minded automation foundation for **Voilà Floor Care** (Midwest Trade Hub Pty Ltd).

The repository keeps the stable technical name `Et-Voila`; customer-facing and operating documentation should use **Voilà Floor Care**.

## Current deployable slice

`Lead enquiry -> deterministic normalisation -> risk/missing-field gate -> optional AI structured extraction -> ServiceM8-ready draft -> human approval`

The repository defaults to **dry-run**. It will not create ServiceM8 jobs unless `VOILA_ALLOW_SERVICEM8_WRITES=true` is set intentionally.

## EGI Cell boundary

Voilà is the reference **field-service Cell**, not a standalone control plane. Generic ServiceM8 transport, bindings, reconciliation, evidence and durable obligations are canonical in the EGI repository; this repository owns Voilà-specific catalogue, pricing, forms/templates, customer policy, website and acceptance tests. Existing direct ServiceM8 code here is a compatibility facade, not the place to evolve shared provider plumbing.

See `docs/EGI_FIELD_SERVICE_BOUNDARY.md`.

## Design rules

- ServiceM8 remains the operational system of record.
- Native ServiceM8 automations are preferred over custom duplication.
- AI may extract/classify/draft; deterministic rules own pricing, safety gates and required fields.
- No autonomous pricing commitments, guarantees, refunds, complaint resolutions or restoration-risk decisions.
- Jim's/franchise-controlled historical data is excluded unless explicitly cleared for migration/use.
- Credentials live only in environment/secrets stores, never in prompts or committed files.
- Shared BVP platform health does **not** prove the Voilà ServiceM8 business-cell path. Production promotion requires fresh scoped write/reread/replay/reconciliation evidence.

## Quick start

```bash
export PYTHONPATH=src
python -m unittest discover -s tests -v
python -m voila_floor.cli --input tests/fixtures_domestic_carpet.json
```

See `docs/DEPLOYMENT.md` for ServiceM8 and n8n setup.
