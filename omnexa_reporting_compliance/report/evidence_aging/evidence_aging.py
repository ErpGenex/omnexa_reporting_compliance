# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

from datetime import datetime, timezone

import frappe
from frappe import _


def execute(filters=None):
	filters = filters or {}
	try:
		days = int(filters.get("older_than_days") or 0)
	except Exception:
		days = 0
	days = max(0, min(3650, days))

	where = ""
	values = {}
	if days:
		values["cutoff_date"] = frappe.utils.add_days(frappe.utils.today(), -days)
		where = "WHERE e.collected_on IS NOT NULL AND e.collected_on <= %(cutoff_date)s"

	rows = frappe.db.sql(
		f"""
		SELECT
			e.company AS company,
			e.control AS control,
			e.exception AS exception,
			e.remediation AS remediation,
			e.collected_on AS collected_on,
			e.attachment AS attachment,
			e.name AS evidence
		FROM `tabCompliance Evidence` e
		{where}
		ORDER BY IFNULL(e.collected_on, '1900-01-01') ASC, e.modified DESC
		LIMIT 2000
		""",
		values=values,
		as_dict=True,
	)
	columns = [
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 160},
		{"label": _("Control"), "fieldname": "control", "fieldtype": "Link", "options": "Compliance Control", "width": 200},
		{"label": _("Exception"), "fieldname": "exception", "fieldtype": "Link", "options": "Compliance Exception", "width": 200},
		{"label": _("Remediation"), "fieldname": "remediation", "fieldtype": "Link", "options": "Compliance Remediation", "width": 200},
		{"label": _("Collected On"), "fieldname": "collected_on", "fieldtype": "Date", "width": 120},
		{"label": _("Attachment"), "fieldname": "attachment", "fieldtype": "Data", "width": 220},
		{"label": _("Evidence"), "fieldname": "evidence", "fieldtype": "Link", "options": "Compliance Evidence", "width": 200},
	]
	return columns, rows

