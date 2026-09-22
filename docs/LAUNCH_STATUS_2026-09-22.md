# Voilà Floor Care — Launch Readiness Status

Last verified: 22 September 2026

## Verified green

- Cloudflare Pages origin `https://voila-floor.pages.dev/` is healthy.
- `/bvp-deployment.json` reports source branch `main` and source commit `18a60db5a37b5bfebc1c53b2ce449d1de34b3142`, matching the latest verified repository commit at the time of audit.
- Main repository test workflow passes on that commit.
- Robots and sitemap assets are present.
- Google Workspace DNS publishes Google MX, SPF, DKIM and DMARC records.

## Red blockers

### 1. Custom domain is not serving the Pages site

Both `https://voilafloor.com.au/` and `https://www.voilafloor.com.au/` returned Cloudflare HTTP 522 during the live audit.

Public DNS is Cloudflare-authoritative. `www.voilafloor.com.au` is a CNAME to `voila-floor.pages.dev`, while the apex is proxied through Cloudflare. The Pages origin itself is healthy, so the custom-domain routing / Cloudflare configuration must be repaired before public launch.

### 2. Production enquiry ingress is not armed

The latest Customer Zero GitHub Actions probe reached `https://voila-floor.pages.dev/api/enquiry` but received:

`HTTP 503 — {"error":"Enquiry service is not configured"}`

This confirms the website function is live but `N8N_LEAD_WEBHOOK_URL` is not configured in the Cloudflare Pages production environment. The probe therefore fails by design rather than creating an uncontrolled downstream job.

## Required exit gates

1. Repair the Cloudflare custom-domain binding/routing so apex and `www` serve the healthy Pages deployment.
2. Add `N8N_LEAD_WEBHOOK_URL` as a Cloudflare Pages production secret only after confirming the production n8n webhook.
3. Re-run the Customer Zero ingress probe and require a PASS with a correlation ID.
4. Re-test one synthetic enquiry end-to-end without customer contact, scheduling, invoicing or payment.
5. Confirm canonical URL, sitemap, Search Console and Google Business Profile website URL after custom-domain recovery.

Do not mark Voilà public-launch ready while either the 522 custom-domain error or the failed production ingress probe remains.
