# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

import frappe
from frappe import _


def _table_exists(table_name: str) -> bool:
	return bool(frappe.db.sql("show tables like %s", (table_name,)))


def execute(filters=None):
	if not _table_exists("tabCompliance Remediation"):
		return _columns(), []
	rows = frappe.db.sql(
		"""
		SELECT
			r.company AS company,
			r.exception AS exception,
			r.status AS status,
			r.owner_user AS owner_user,
			r.due_date AS due_date,
			r.completed_on AS completed_on,
			r.name AS remediation
		FROM `tabCompliance Remediation` r
		WHERE r.status IN ('Open', 'In Progress')
		ORDER BY IFNULL(r.due_date, '9999-12-31') ASC, r.modified DESC
		LIMIT 1000
		""",
		as_dict=True,
	)
	return _columns(), rows


def _columns():
	return [
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 160},
		{"label": _("Exception"), "fieldname": "exception", "fieldtype": "Link", "options": "Compliance Exception", "width": 220},
		{"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 120},
		{"label": _("Owner"), "fieldname": "owner_user", "fieldtype": "Link", "options": "User", "width": 140},
		{"label": _("Due Date"), "fieldname": "due_date", "fieldtype": "Date", "width": 110},
		{"label": _("Completed On"), "fieldname": "completed_on", "fieldtype": "Date", "width": 110},
		{"label": _("Remediation"), "fieldname": "remediation", "fieldtype": "Link", "options": "Compliance Remediation", "width": 200},
	]

