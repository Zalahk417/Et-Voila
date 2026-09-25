# Voilà Floor Care — EGI field-service reference Cell

Voilà Floor Care is the reference implementation of the EGI `field-service` archetype.

## Ownership boundary

**EGI Kernel owns**
- capability and binding contracts;
- credential resolution and authorised execution paths;
- generic ServiceM8 transport/retry/reconciliation primitives;
- idempotency, runtime evidence and durable obligations;
- Jarvis preflight and browser-last routing.

**Voilà owns**
- service/material catalogue and pricing;
- tax/inventory policy;
- categories, queues, badges, forms and job templates;
- customer communication rules;
- service-area, brand and market rules;
- project-specific desired state and acceptance tests.

ServiceM8 remains the operational system of record for customers, jobs, schedule, quotes and field operations.

## Current migration state

The production ServiceM8 binding is already registered and proven through the governed backend path. The local `src/voila_floor/servicem8.py` and `scripts/servicem8_bootstrap.py` remain compatibility facades so that architecture cleanup cannot break a live path.

Generic provider primitives now live canonically in:

`Zalahk417-ai-operations-system/automation/providers/servicem8/`

The local facade is removed only after an independently verified package/runtime cutover. Until then, new generic ServiceM8 transport or reconciliation logic must be added to EGI first rather than expanded here.

## Run rule

A ServiceM8 population, diagnostic, bootstrap, Customer Zero or repair chat is a temporary **Run**, not another Voilà sub-project. Durable configuration belongs in this repository/ServiceM8; evidence and unresolved work return to EGI.
