# Voila Floor — Cloudflare Pages Deployment

## Pages project
- Repository: `Zalahk417/Et-Voila`
- Production branch: `main`
- Root directory: `website`
- Build command: `python build.py`
- Build output directory: `dist`
- Pages Functions directory: `functions`

## Runtime configuration
Set the following as a **Cloudflare Pages secret**, not a plain browser variable and not in GitHub:

- `N8N_LEAD_WEBHOOK_URL` — production n8n webhook for Voila Floor lead intake.

Until this secret exists, the website may be previewed but enquiry forwarding must be treated as staging/incomplete.

## Deployment sequence
1. Create/import the Cloudflare Pages project from the GitHub repository.
2. Apply the project settings above.
3. Deploy to the generated `*.pages.dev` preview/production hostname first.
4. Smoke-test `/`, service pages, `/blog/`, `/case-studies/`, `/contact/`, `/sitemap.xml`, `/robots.txt`, `/api/enquiry` and `/bvp-deployment.json`.
5. Add `N8N_LEAD_WEBHOOK_URL` only after the n8n production webhook has been reviewed.
6. Verify `/bvp-deployment.json` reports the exact current GitHub `main` commit SHA; a mismatch is RED and must not be promoted.
7. Test one synthetic enquiry end-to-end before accepting customer traffic.
8. Add the final custom domain only after the canonical production domain is confirmed.
9. Verify Search Console, sitemap submission, Google Business Profile website URL and conversion analytics after launch.

## Safety
- Never expose ServiceM8, n8n or model API credentials in frontend code.
- The website sends enquiry data only to the server-side Pages Function.
- Pricing, restoration risk and customer commitments remain human-gated.
