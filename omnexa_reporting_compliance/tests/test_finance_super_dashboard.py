from frappe.tests.utils import FrappeTestCase

from omnexa_reporting_compliance.api import get_finance_super_dashboard


class TestFinanceSuperDashboard(FrappeTestCase):
	def test_super_dashboard_has_summary(self):
		out = get_finance_super_dashboard()
		self.assertIn("summary", out)
		self.assertIn("apps", out)
		self.assertGreaterEqual(int(out["summary"]["apps_count"]), 1)
