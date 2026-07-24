# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

import json
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
	rc = os.path.join(base, "reporting_compliance")
	json_paths = [
		# DocTypes
		os.path.join(rc, "doctype", "compliance_control", "compliance_control.json"),
		os.path.join(rc, "doctype", "compliance_control_test", "compliance_control_test.json"),
		os.path.join(rc, "doctype", "compliance_exception", "compliance_exception.json"),
		os.path.join(rc, "doctype", "compliance_remediation", "compliance_remediation.json"),
		os.path.join(rc, "doctype", "compliance_evidence", "compliance_evidence.json"),
		# Reports
		os.path.join(rc, "report", "controls_coverage", "controls_coverage.json"),
		os.path.join(rc, "report", "failed_control_tests", "failed_control_tests.json"),
		os.path.join(rc, "report", "open_remediations", "open_remediations.json"),
		os.path.join(rc, "report", "evidence_aging", "evidence_aging.json"),
	]
	for path in json_paths:
		with open(path, encoding="utf-8") as handle:
			payload = json.load(handle) or {}
		if isinstance(payload, dict) and payload.get("name") and not payload.get("doctype") and "/workspace/" in path.replace("\\", "/"):
			if frappe.db.exists("Workspace", payload["name"]):
				workspace = frappe.get_doc("Workspace", payload["name"])
				workspace.update(payload)
				workspace.save(ignore_permissions=True)
			else:
				payload["doctype"] = "Workspace"
				frappe.get_doc(payload).insert(ignore_permissions=True)
			continue
		import_file_by_path(path, force=True)
