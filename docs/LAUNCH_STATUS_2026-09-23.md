# Voilà Floor Care — Launch Status — 23 September 2026

## Executive state
Architecture and staging are substantially complete, but V1 is not launch-green. The clean ServiceM8 tenant is connected; the public Pages origin is healthy; the machine-readable control plane is fail-closed. Remaining blockers are runtime configuration and proof.

## Verified now
- ServiceM8 connector resolves to the clean tenant with Paul-Michael Haik as the sole staff member and only the SAMPLE Help Guide Job.
- Live ServiceM8 has four categories, three badges, three default-style queues, zero Forms, zero Job Templates, default tax NONE/0%, and Knowledge Management inactive.
- GitHub live ServiceM8 state is recorded in `config/servicem8.production.json` schema v2 and production writes remain disabled by default.
- Cloudflare Pages origin `https://voila-floor.pages.dev/` is healthy.
- Final deployment recheck reports source branch `main` and source commit `1f3503630d40a67a7c3edbab41eb2fcf8da9f4cb`, confirming GitHub → Cloudflare Pages auto-deployment is current.
- The current site serves the Voilà Floor Care brand, Australian-English customer copy, service catalogue, call/text route, Privacy and Terms pages.
- Canva has a native Voilà Floor Care Brand Kit and a 10-page Master Brand Guidelines design. Its palette matches the website source.
- Notion remains the governance/staging authority and now contains the 23 September full-project consolidation audit. Four verified-empty duplicate staging databases were renamed `DEPRECATED — EMPTY`; canonical populated masters contain 35 registry, 70 catalogue, 3 supplier and 46 knowledge-control records.
- n8n cloud host and readiness endpoints both return `status: ok`; host availability is GREEN, while workflow/credential wiring remains unproven.

## RED / launch blockers
1. `https://voilafloor.com.au/` and `https://www.voilafloor.com.au/` return Cloudflare HTTP 522. Public DNS resolves through Cloudflare and `www` currently CNAMEs to `voila-floor.pages.dev`; the remaining fault is in custom-domain/Pages routing rather than GitHub deployment availability.
2. Website enquiry POST path is not certified end-to-end to n8n and ServiceM8 in this audit. The latest recorded probe was fail-closed/unarmed.
3. ServiceM8 live tenant is not populated with the approved Voilà job templates, forms, floor-care queues/taxonomy and launch configuration.
4. ServiceM8 tax is not launch-ready: NONE/0% is currently the default.
5. Knowledge Management is inactive; Premium/feature-trial configuration still needs runtime setup and verification.
6. Google Workspace admin runtime is not connected here. Gmail/Drive connector currently resolves to the personal `pmhaik@gmail.com` identity. Test messages were sent to `hello@`, `bookings@` and `accounts@voilafloor.com.au`, but no inbound alias delivery or outbound send-as evidence is visible, so Voilà role-mail routing/reply identity is not certified.
7. Opera Browser Connector is not connected and the Remote Desktop device is offline, preventing authenticated UI repair of Cloudflare, n8n, Google Admin and ServiceM8 configuration from this session.

## Release rule
Do not mark V1 GREEN until the custom domain, enquiry ingress, ServiceM8 population/tax/add-ons and Google Workspace routing have direct runtime evidence and one synthetic Customer Zero completes without duplicate or unintended customer-facing consequences.