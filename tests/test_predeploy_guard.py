import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREDEPLOY = ROOT / "website" / "predeploy.py"
SPEC = importlib.util.spec_from_file_location("website_predeploy", PREDEPLOY)
predeploy = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(predeploy)


class WebsitePredeployGuardTest(unittest.TestCase):
    def test_main_branch_is_blocked_without_explicit_launch_authorisation(self):
        with self.assertRaises(RuntimeError):
            predeploy.require_public_launch_authorisation({"CF_PAGES_BRANCH": "main"})

    def test_main_branch_is_allowed_with_explicit_launch_authorisation(self):
        predeploy.require_public_launch_authorisation(
            {"CF_PAGES_BRANCH": "main", "VOILA_PUBLIC_LAUNCH": "true"}
        )

    def test_preview_branch_remains_buildable(self):
        predeploy.require_public_launch_authorisation(
            {"CF_PAGES_BRANCH": "fix/sep11-deployment-brand-guard"}
        )


if __name__ == "__main__":
    unittest.main()
