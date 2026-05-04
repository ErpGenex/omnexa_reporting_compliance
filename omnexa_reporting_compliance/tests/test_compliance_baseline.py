from frappe.tests.utils import FrappeTestCase
import frappe
from frappe.modules.import_file import import_file_by_path
import os


def _ensure_compliance_doctypes():
	base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reporting_compliance"))
	for rel in (
		("doctype", "compliance_control", "compliance_control.json"),
		("doctype", "compliance_control_test", "compliance_control_test.json"),
		("doctype", "compliance_exception", "compliance_exception.json"),
		("doctype", "compliance_remediation", "compliance_remediation.json"),
		("doctype", "compliance_evidence", "compliance_evidence.json"),
	):
		import_file_by_path(os.path.join(base, *rel), force=True)


class TestComplianceBaseline(FrappeTestCase):
	def test_doctypes_exist(self):
		# meta lookup should succeed after migrate
		_ensure_compliance_doctypes()
		for dt in (
			"Compliance Control",
			"Compliance Control Test",
			"Compliance Exception",
			"Compliance Remediation",
			"Compliance Evidence",
		):
			meta = frappe.get_meta(dt)
			self.assertEqual(meta.name, dt)

	def test_reports_execute(self):
		from omnexa_reporting_compliance.reporting_compliance.report.controls_coverage.controls_coverage import (
			execute as controls_execute,
		)
		from omnexa_reporting_compliance.reporting_compliance.report.evidence_aging.evidence_aging import (
			execute as evidence_execute,
		)
		from omnexa_reporting_compliance.reporting_compliance.report.failed_control_tests.failed_control_tests import (
			execute as failed_execute,
		)
		from omnexa_reporting_compliance.reporting_compliance.report.open_remediations.open_remediations import (
			execute as open_execute,
		)

		for fn, filters in (
			(controls_execute, None),
			(failed_execute, None),
			(open_execute, None),
			(evidence_execute, {"older_than_days": 0}),
		):
			cols, rows = fn(filters)
			self.assertIsInstance(cols, list)
			self.assertIsInstance(rows, list)

