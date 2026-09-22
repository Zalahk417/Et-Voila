import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
DIST = WEBSITE / "dist"
SERVICEM8_URL = "https://book.servicem8.com/request_booking?uuid=725f7ba5-b2b6-4997-926c-1f3f26af55eb"


class WebsiteBuildAcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, "build.py"],
            cwd=WEBSITE,
            check=True,
        )

    def test_homepage_has_current_brand_and_primary_actions(self):
        html = (DIST / "index.html").read_text(encoding="utf-8")
        self.assertIn("Voilà Floor Care", html)
        self.assertIn('<div class="voila-contact-strip">', html)
        self.assertIn('<section class="voila-hero-banner"', html)
        self.assertIn("tile-grout-restoration-03.webp", html)
        self.assertNotIn(SERVICEM8_URL, html)
        self.assertIn("0402 221 071", html)
        self.assertIn('<a class="voila-sticky-quote" href="/contact/"', html)
        self.assertIn('<a class="voila-primary-cta" href="/contact/">Start an Enquiry</a>', html)
        self.assertIn('/terms/', html)

    def test_contact_form_uses_bvp_enquiry_endpoint(self):
        contact = (DIST / "contact" / "index.html").read_text(encoding="utf-8")
        javascript = (DIST / "assets" / "site.js").read_text(encoding="utf-8")
        self.assertIn("data-enquiry-form", contact)
        self.assertNotIn(SERVICEM8_URL, contact)
        self.assertIn("/api/enquiry", javascript)

    def test_bvp_deployment_identity_is_emitted(self):
        deployment = json.loads((DIST / "bvp-deployment.json").read_text(encoding="utf-8"))
        self.assertEqual(deployment["schema_version"], 1)
        self.assertIn(deployment["provider"], {"cloudflare-pages", "local-ci"})
        self.assertTrue(deployment["source_commit"])
        self.assertTrue(deployment["source_branch"])

    def test_terms_page_exists_and_preserves_consumer_rights(self):
        terms = (DIST / "terms" / "index.html").read_text(encoding="utf-8")
        self.assertIn("Terms &amp; Conditions", terms)
        self.assertIn("Australian Consumer Law", terms)
        self.assertIn("Midwest Trade Hub Pty Ltd", terms)

    def test_customer_facing_legacy_brand_is_not_on_homepage(self):
        html = (DIST / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("Voilá Floor Care", html)
        self.assertNotIn("Voila Floor Cleaning & Restoration", html)


if __name__ == "__main__":
    unittest.main()
