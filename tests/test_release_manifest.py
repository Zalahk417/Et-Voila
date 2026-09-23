import json
import os
import unittest


ROOT = os.path.dirname(os.path.dirname(__file__))
MANIFEST = os.path.join(ROOT, "config", "release.production.json")


class ReleaseManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(MANIFEST, "r", encoding="utf-8") as f:
            cls.m = json.load(f)

    def test_manifest_uses_current_repository_identity(self):
        self.assertEqual(self.m["repository"], "Zalahk417/VOILA-FLOOR-CARE")

    def test_launch_green_is_blocked_by_open_root_variables(self):
        open_states = {"UNRESOLVED", "NOT_READY", "NOT_PROVEN"}
        roots = self.m["root_variables"]
        has_open_root = any(v["status"] in open_states for v in roots.values())
        if has_open_root:
            self.assertNotEqual(self.m["release_state"], "LAUNCH_GREEN")

    def test_launch_green_is_blocked_by_open_runtime_gates(self):
        closed_states = {"PROVEN", "PASSED", "GREEN"}
        gates = self.m["runtime_gates"]
        all_closed = all(v in closed_states for v in gates.values())
        if not all_closed:
            self.assertNotEqual(self.m["release_state"], "LAUNCH_GREEN")

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
