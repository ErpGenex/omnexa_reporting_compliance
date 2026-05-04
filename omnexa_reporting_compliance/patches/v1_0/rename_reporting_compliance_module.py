# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

"""Align DB module name with Frappe module path (fixes FormMeta template path)."""

import frappe

_OLD = "Omnexa Reporting Compliance"
_NEW = "Reporting Compliance"

_DOCTYPES = (
	"Compliance Control",
	"Compliance Control Test",
	"Compliance Exception",
	"Compliance Remediation",
	"Compliance Evidence",
)

_REPORTS = (
	"Controls Coverage",
	"Failed Control Tests",
	"Open Remediations",
	"Evidence Aging",
)


def execute():
	frappe.db.sql(
		"UPDATE `tabDocType` SET `module`=%s WHERE `module`=%s AND `name` IN ({})".format(
			",".join(["%s"] * len(_DOCTYPES))
		),
		(_NEW, _OLD, *_DOCTYPES),
	)
	frappe.db.sql(
		"UPDATE `tabReport` SET `module`=%s WHERE `module`=%s AND `name` IN ({})".format(
			",".join(["%s"] * len(_REPORTS))
		),
		(_NEW, _OLD, *_REPORTS),
	)
	frappe.clear_cache()
