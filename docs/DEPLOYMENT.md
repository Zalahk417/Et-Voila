# Deployment — Lead Intake v0.1

## Implemented

- deterministic normalisation and required-field checks;
- restoration/contamination/guarantee risk routing;
- stable idempotency key;
- ServiceM8-compatible draft job payload;
- SQLite audit logging with duplicate protection;
- ServiceM8 client with writes blocked by default;
- OpenAI Responses API structured extraction helper with `store=false`;
- n8n Stage-1 dry-run import.

## ServiceM8

For a private integration to the business' own account, generate an API key in ServiceM8 **Settings -> API Keys** and store it as `SERVICEM8_API_KEY` in runtime secrets.

Base URL: `https://api.servicem8.com/api_1.0`

Authentication: `X-API-Key: <secret>`

Current ServiceM8 endpoints used by the code are `POST /company.json` and `POST /job.json`. Job creation requires `status`; this implementation creates draft jobs as `Quote` and omits `company_uuid` until client resolution is complete.

Private API-key integrations suit REST calls to your own account. Some Webhooks/Messaging capabilities require OAuth/public-application style integration; begin read-only/private during the Academy, then promote only when the production event architecture justifies it.

## Promotion sequence

1. **Local dry-run:** run tests and evaluate 30–50 sanitised enquiries.
2. **Read-only ServiceM8:** configure API key; keep `VOILA_ALLOW_SERVICEM8_WRITES=false`.
3. **Test writes:** independent Voila Floor test customer/job only; explicitly enable writes in test runtime.
4. **n8n orchestration:** import `n8n/voila-floor-lead-intake-stage1.json` and keep it inactive until reviewed.
5. **Controlled production:** only after replay, failure, privacy and human-approval tests pass.

## Intentionally not enabled

Automatic quote sending, autonomous pricing, guarantees, high-risk restoration acceptance, refunds/complaints, Jim's data migration and autonomous customer messaging.
