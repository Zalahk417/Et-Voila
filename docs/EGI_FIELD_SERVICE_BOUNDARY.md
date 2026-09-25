# Voilà Floor Care — EGI field-service boundary

Voilà Floor Care is the reference implementation of the EGI `field-service` Cell archetype.

Generic ServiceM8 transport, canonical architecture, ports/adapters, binding contracts, reconciliation primitives, evidence rules and durable obligations live in:

`Zalahk417/Zalahk417-ai-operations-system`

Relevant canonical objects:

- `11_portfolio/archetypes/field-service.yaml`
- `11_portfolio/projects/voila-floor-care.yaml`
- `11_portfolio/twins/voila-floor-care.yaml`
- `08_adapters/providers/servicem8.yaml`
- `08_adapters/SERVICEM8_SHARED_BOUNDARY.md`
- `tools/lib/servicem8_n8n_client.py`

## This repository owns

- Voilà service catalogue and pricing/business rules;
- categories, queues, badges, forms and templates;
- Voilà-specific lead/job/customer policy;
- website, brand and local market content;
- project-specific acceptance tests and desired-state manifests.

## This repository does not own

- generic ServiceM8 authentication or credential resolution;
- generic retry/backoff, pagination or response aggregation;
- generic n8n transport;
- portfolio-wide idempotency/reconciliation contracts;
- Jarvis, EGI governance or cross-project durable obligation logic.

The existing direct ServiceM8 client and bootstrap scripts are retained as **compatibility facades** for current tests and controlled local/runtime paths. They must not become a second evolving provider SDK. Shared transport changes are made in EGI first and then deliberately consumed or mirrored here only when a safe package/runtime path exists.

## Migration rule

Do not delete a proven compatibility path merely to satisfy architecture cleanliness. Replace it only after the EGI shared transport has a tested consumption path for this repository and the same target-state read-back proves no regression.
