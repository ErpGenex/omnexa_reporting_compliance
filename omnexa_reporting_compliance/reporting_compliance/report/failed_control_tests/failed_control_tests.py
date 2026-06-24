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
		{"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 160},
		{"label": _("Control"), "fieldname": "control", "fieldtype": "Link", "options": "Compliance Control", "width": 220},
		{"label": _("Test Date"), "fieldname": "test_date", "fieldtype": "Date", "width": 110},
		{"label": _("Tester"), "fieldname": "tester", "fieldtype": "Link", "options": "User", "width": 140},
		{"label": _("Result"), "fieldname": "result", "fieldtype": "Data", "width": 90},
		{"label": _("Test"), "fieldname": "control_test", "fieldtype": "Link", "options": "Compliance Control Test", "width": 200},
	]
	filters = prepare_filters(filters)
	conditions, params = sql_conditions(
		filters,
		"Compliance Control Test",
		date_field="test_date",
		company=True,
		branch=False,
		table_alias="ct",
	)
	conditions.append("ct.result = 'Fail'")
	rows = frappe.db.sql(
		f"""
		SELECT
			ct.company AS company,
			ct.control AS control,
			ct.test_date AS test_date,
			ct.tester AS tester,
			ct.result AS result,
			ct.name AS control_test
		FROM `tabCompliance Control Test` ct
		WHERE {' AND '.join(conditions)}
		ORDER BY ct.test_date DESC, ct.modified DESC
		LIMIT 1000
		""",
		params,
		as_dict=True,
	)
	chart = auto_chart_for_columns(rows, columns)
	return columns, rows, None, chart