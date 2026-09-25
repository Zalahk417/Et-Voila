from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestEgiBoundary(unittest.TestCase):
    def test_boundary_documented(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        boundary = (ROOT / "docs" / "EGI_FIELD_SERVICE_BOUNDARY.md").read_text(encoding="utf-8")
        self.assertIn("reference **field-service Cell**", readme)
        self.assertIn("Generic ServiceM8 transport", boundary)
        self.assertIn("compatibility facades", boundary)

    def test_local_transport_is_explicitly_noncanonical(self):
        client = (ROOT / "src" / "voila_floor" / "servicem8.py").read_text(encoding="utf-8")
        bootstrap = (ROOT / "scripts" / "servicem8_bootstrap.py").read_text(encoding="utf-8")
        self.assertIn("compatibility facade", client)
        self.assertIn("Generic ServiceM8 transport", client)
        self.assertIn("desired-state bootstrap compatibility path", bootstrap)
        self.assertIn("Generic ServiceM8 transport", bootstrap)


if __name__ == "__main__":
    unittest.main()
