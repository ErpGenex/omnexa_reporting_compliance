# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

import frappe
from frappe import _

from omnexa_core.omnexa_core.utils.report_charts import auto_chart_for_columns

from omnexa_core.omnexa_core.report_print.report_query_filters import (
	get_all_filters,
	policy_version_filters,
	prepare_filters,
	sql_conditions,
)



def execute(filters=None):
	columns = [
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 180},
		{"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 110},
		{"label": _("Risk Level"), "fieldname": "risk_level", "fieldtype": "Data", "width": 120},
		{"label": _("Controls"), "fieldname": "controls_count", "fieldtype": "Int", "width": 120},
	]
	filters = prepare_filters(filters)
	conditions, params = sql_conditions(filters, "Compliance Control", date_field="creation", company=True, branch=True)
	rows = frappe.db.sql(
		f"""
		SELECT
			cc.company AS company,
			cc.status AS status,
			cc.risk_level AS risk_level,
			COUNT(*) AS controls_count
		FROM `tabCompliance Control`
		WHERE {' AND '.join(conditions)}
		GROUP BY cc.company, cc.status, cc.risk_level
		ORDER BY cc.company, cc.status, cc.risk_level
		""",
		params,
		as_dict=True,
	)
	chart = auto_chart_for_columns(rows, columns)
	return columns, rows, None, chart