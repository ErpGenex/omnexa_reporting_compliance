from frappe.tests.utils import FrappeTestCase

from omnexa_reporting_compliance import hooks, license_gate


class TestReportingComplianceLicenseSmoke(FrappeTestCase):
	def test_license_gate_is_wired(self):
		self.assertEqual(hooks.before_request, ["omnexa_reporting_compliance.license_gate.before_request"])
		self.assertEqual(license_gate._APP, "omnexa_reporting_compliance")
