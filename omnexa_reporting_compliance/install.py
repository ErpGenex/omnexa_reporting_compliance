# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

import os

import frappe
from frappe.modules.import_file import import_file_by_path


SUPPORTED_FRAPPE_MAJOR = 15


def enforce_supported_frappe_version():
	"""Fail early when running on an unsupported Frappe major release."""
	version_text = (getattr(frappe, "__version__", "") or "").strip()
	if not version_text:
		return

	major_token = version_text.split(".", 1)[0]
	try:
		major = int(major_token)
	except ValueError:
		return

	if major != SUPPORTED_FRAPPE_MAJOR:
		frappe.throw(
			f"Unsupported Frappe version '{version_text}' for omnexa_reporting_compliance. "
			"Supported range is >=15.0,<16.0.",
			frappe.ValidationError,
		)


def after_migrate():
	"""Ensure core compliance DocTypes/Reports are imported from this app layout."""
	base = os.path.dirname(__file__)
	json_paths = [
		# DocTypes
		os.path.join(base, "doctype", "compliance_control", "compliance_control.json"),
		os.path.join(base, "doctype", "compliance_control_test", "compliance_control_test.json"),
		os.path.join(base, "doctype", "compliance_exception", "compliance_exception.json"),
		os.path.join(base, "doctype", "compliance_remediation", "compliance_remediation.json"),
		os.path.join(base, "doctype", "compliance_evidence", "compliance_evidence.json"),
		# Reports
		os.path.join(base, "report", "controls_coverage", "controls_coverage.json"),
		os.path.join(base, "report", "failed_control_tests", "failed_control_tests.json"),
		os.path.join(base, "report", "open_remediations", "open_remediations.json"),
		os.path.join(base, "report", "evidence_aging", "evidence_aging.json"),
	]
	for path in json_paths:
		import_file_by_path(path, force=True)
