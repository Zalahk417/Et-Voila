# Voila Floor — Cloudflare Pages Deployment

## Current release state

**HOLD — JCC Geraldton remains the only live customer-facing brand.**

Voilà Floor Care may be built and reviewed on Cloudflare preview deployments, but it must not replace the current JCC Geraldton customer-facing production presence until an explicit owner-approved cutover.

## Pages project
- Repository: `Zalahk417/Et-Voila`
- Production branch: `main`
- Root directory: `website`
- Build command: `python predeploy.py`
- Build output directory: `dist`
- Pages Functions directory: `functions`

`predeploy.py` is a fail-closed production guard. Cloudflare preview branches build normally. A build from `main` is refused unless the production environment contains:

- `VOILA_PUBLIC_LAUNCH=true`

Do **not** set that variable while JCC Geraldton remains the live customer-facing brand. Removing or leaving it unset keeps the current production deployment protected while allowing preview QA.

## Runtime configuration
Set the following as a **Cloudflare Pages secret**, not a plain browser variable and not in GitHub:

- `N8N_LEAD_WEBHOOK_URL` — production n8n webhook for Voila Floor lead intake.

Until this secret exists, the website may be previewed but enquiry forwarding must be treated as staging/incomplete.

## Deployment sequence
1. Create/import the Cloudflare Pages project from the GitHub repository.
2. Apply the project settings above, especially `python predeploy.py` as the build command.
3. Leave `VOILA_PUBLIC_LAUNCH` unset while JCC Geraldton is the live brand.
4. Deploy feature branches to generated `*.pages.dev` preview hostnames for QA.
5. Smoke-test `/`, service pages, `/blog/`, `/case-studies/`, `/contact/`, `/terms/`, `/sitemap.xml`, `/robots.txt` and `/api/enquiry`.
6. Add `N8N_LEAD_WEBHOOK_URL` only after the n8n production webhook has been reviewed.
7. Test one synthetic enquiry end-to-end before accepting customer traffic.
8. At the approved brand cutover only, set `VOILA_PUBLIC_LAUNCH=true`, deploy `main`, verify the production target, then add/confirm the final custom domain.
9. Verify Search Console, sitemap submission, Google Business Profile website URL and conversion analytics after launch.

## Safety
- Never expose ServiceM8, n8n or model API credentials in frontend code.
- The website sends enquiry data only to the server-side Pages Function.
- Pricing, restoration risk and customer commitments remain human-gated.
- A green GitHub Actions test run does not itself authorise a public Voilà launch.
- Never expose Voilà branding on the current JCC Geraldton customer-facing production surface before the approved cutover.
