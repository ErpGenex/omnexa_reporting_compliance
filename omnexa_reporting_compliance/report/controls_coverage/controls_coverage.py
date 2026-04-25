# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

import frappe
from frappe import _


def _table_exists(table_name: str) -> bool:
	return bool(frappe.db.sql("show tables like %s", (table_name,)))


def execute(filters=None):
	if not _table_exists("tabCompliance Control"):
		return _columns(), []
	rows = frappe.db.sql(
		"""
		SELECT
			cc.company AS company,
			cc.status AS status,
			cc.risk_level AS risk_level,
			COUNT(*) AS controls_count
		FROM `tabCompliance Control` cc
		GROUP BY cc.company, cc.status, cc.risk_level
		ORDER BY cc.company, cc.status, cc.risk_level
		""",
		as_dict=True,
	)
	return _columns(), rows


def _columns():
	return [
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 180},
		{"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 110},
		{"label": _("Risk Level"), "fieldname": "risk_level", "fieldtype": "Data", "width": 120},
		{"label": _("Controls"), "fieldname": "controls_count", "fieldtype": "Int", "width": 120},
	]

