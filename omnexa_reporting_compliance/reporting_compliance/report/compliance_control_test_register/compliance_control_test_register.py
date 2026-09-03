# Copyright (c) 2026, ErpGenEx
# Auto-generated Global Excellence report pack

import frappe
from frappe import _


def execute(filters=None):
	data = frappe.db.sql(
		"""
		SELECT `name`, `company`, `branch`, `control`, `test_date`, `result`
		FROM `tabCompliance Control Test`
		ORDER BY modified DESC
		LIMIT 500
		""",
		as_dict=True,
	)
	columns = [
		{"label": _("Name"), "fieldname": "name", "fieldtype": "Link", "width": 140},
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "width": 120},
		{"label": _("Branch"), "fieldname": "branch", "fieldtype": "Link", "width": 120},
		{"label": _("Control"), "fieldname": "control", "fieldtype": "Link", "width": 120},
		{"label": _("Test Date"), "fieldname": "test_date", "fieldtype": "Date", "width": 120},
		{"label": _("Result"), "fieldname": "result", "fieldtype": "Select", "width": 120}
	]
	return columns, data
