# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

import frappe
from frappe import _

from omnexa_core.omnexa_core.report_print.report_query_filters import (
	get_all_filters,
	policy_version_filters,
	prepare_filters,
	sql_conditions,
)



def execute(filters=None):
	columns = [
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 160},
		{"label": _("Exception"), "fieldname": "exception", "fieldtype": "Link", "options": "Compliance Exception", "width": 220},
		{"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 120},
		{"label": _("Owner"), "fieldname": "owner_user", "fieldtype": "Link", "options": "User", "width": 140},
		{"label": _("Due Date"), "fieldname": "due_date", "fieldtype": "Date", "width": 110},
		{"label": _("Completed On"), "fieldname": "completed_on", "fieldtype": "Date", "width": 110},
		{"label": _("Remediation"), "fieldname": "remediation", "fieldtype": "Link", "options": "Compliance Remediation", "width": 200},
	]
	filters = prepare_filters(filters)
	conditions, params = sql_conditions(filters, "Compliance Remediation", date_field="creation", company=True, branch=True)
	rows = frappe.db.sql(
		f"""
		SELECT
			r.company AS company,
			r.exception AS exception,
			r.status AS status,
			r.owner_user AS owner_user,
			r.due_date AS due_date,
			r.completed_on AS completed_on,
			r.name AS remediation
		FROM `tabCompliance Remediation`
		WHERE {' AND '.join(conditions)}
		GROUP BY 1
		ORDER BY IFNULL(r.due_date, '9999-12-31') ASC, r.modified DESC
		LIMIT 1000
		""",
		params,
		as_dict=True,
	)
	return columns, rows
