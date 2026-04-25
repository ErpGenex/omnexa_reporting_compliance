# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

import frappe
from frappe import _


def _table_exists(table_name: str) -> bool:
	return bool(frappe.db.sql("show tables like %s", (table_name,)))


def execute(filters=None):
	if not _table_exists("tabCompliance Control Test"):
		return _columns(), []
	rows = frappe.db.sql(
		"""
		SELECT
			ct.company AS company,
			ct.control AS control,
			ct.test_date AS test_date,
			ct.tester AS tester,
			ct.result AS result,
			ct.name AS control_test
		FROM `tabCompliance Control Test` ct
		WHERE ct.result = 'Fail'
		ORDER BY ct.test_date DESC, ct.modified DESC
		LIMIT 1000
		""",
		as_dict=True,
	)
	return _columns(), rows


def _columns():
	return [
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 160},
		{"label": _("Control"), "fieldname": "control", "fieldtype": "Link", "options": "Compliance Control", "width": 220},
		{"label": _("Test Date"), "fieldname": "test_date", "fieldtype": "Date", "width": 110},
		{"label": _("Tester"), "fieldname": "tester", "fieldtype": "Link", "options": "User", "width": 140},
		{"label": _("Result"), "fieldname": "result", "fieldtype": "Data", "width": 90},
		{"label": _("Test"), "fieldname": "control_test", "fieldtype": "Link", "options": "Compliance Control Test", "width": 200},
	]

