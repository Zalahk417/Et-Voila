import json
import os
import unittest


ROOT = os.path.dirname(os.path.dirname(__file__))
MANIFEST = os.path.join(ROOT, "config", "release.production.json")

CLOSED_ROOT_STATES = {"LOCKED", "READY", "PROVEN", "PROVEN_CLEAN"}
CLOSED_RUNTIME_STATES = {"PROVEN", "PASSED", "GREEN"}


class ReleaseManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(MANIFEST, "r", encoding="utf-8") as f:
            cls.m = json.load(f)

    def test_manifest_uses_current_repository_identity(self):
        self.assertEqual(self.m["repository"], "Zalahk417/VOILA-FLOOR-CARE")

    def test_launch_green_requires_explicitly_closed_root_variables(self):
        if self.m["release_state"] == "LAUNCH_GREEN":
            roots = self.m["root_variables"]
            for name, value in roots.items():
                self.assertIn(
                    value["status"],
                    CLOSED_ROOT_STATES,
                    f"root variable {name} is not explicitly closed",
                )

    def test_launch_green_requires_explicitly_closed_runtime_gates(self):
        if self.m["release_state"] == "LAUNCH_GREEN":
            for name, value in self.m["runtime_gates"].items():
                self.assertIn(
                    value,
                    CLOSED_RUNTIME_STATES,
                    f"runtime gate {name} is not explicitly closed",
                )

    def test_unknown_or_provisional_status_is_not_implicitly_green(self):
        unsafe_states = {"PROVISIONAL", "PARTIAL", "UNKNOWN", "ASSUMED", "STAGED"}
        self.assertTrue(unsafe_states.isdisjoint(CLOSED_ROOT_STATES))
        self.assertTrue(unsafe_states.isdisjoint(CLOSED_RUNTIME_STATES))

    def test_mutating_customer_actions_remain_fail_closed_before_customer_zero(self):
        if self.m["runtime_gates"]["full_customer_zero"] != "PASSED":
            safety = self.m["safety"]
            self.assertFalse(safety["production_writes_authorised"])
            self.assertFalse(safety["customer_communications_allowed"])
            self.assertFalse(safety["scheduling_allowed"])
            self.assertFalse(safety["invoicing_allowed"])
            self.assertFalse(safety["payment_allowed"])


if __name__ == "__main__":
    unittest.main()
