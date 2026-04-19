from __future__ import annotations

import frappe


FINANCE_DASHBOARD_METHODS = {
	"omnexa_finance_engine": "omnexa_finance_engine.api.get_regulatory_dashboard",
	"omnexa_credit_engine": "omnexa_credit_engine.api.get_regulatory_dashboard",
	"omnexa_credit_risk": "omnexa_credit_risk.api.get_regulatory_dashboard",
	"omnexa_operational_risk": "omnexa_operational_risk.api.get_regulatory_dashboard",
	"omnexa_alm": "omnexa_alm.api.get_regulatory_dashboard",
	"omnexa_consumer_finance": "omnexa_consumer_finance.api.get_regulatory_dashboard",
	"omnexa_vehicle_finance": "omnexa_vehicle_finance.api.get_regulatory_dashboard",
	"omnexa_mortgage_finance": "omnexa_mortgage_finance.api.get_regulatory_dashboard",
	"omnexa_factoring": "omnexa_factoring.api.get_regulatory_dashboard",
	"omnexa_sme_retail_finance": "omnexa_sme_retail_finance.api.get_regulatory_dashboard",
}


@frappe.whitelist()
def get_finance_super_dashboard() -> dict:
	"""Unified cross-app governance/regulatory snapshot for all finance apps."""
	apps = []
	installed = set(frappe.get_installed_apps() or [])
	for app_name, method_path in FINANCE_DASHBOARD_METHODS.items():
		if app_name not in installed:
			continue
		try:
			method = frappe.get_attr(method_path)
			payload = method()
			apps.append(payload)
		except Exception:
			frappe.log_error(frappe.get_traceback(), f"finance_super_dashboard_{app_name}")
			apps.append(
				{
					"app": app_name,
					"error": "dashboard_unavailable",
					"compliance_score": 0,
					"governance": {
						"policies_total": 0,
						"policies_pending": 0,
						"policies_approved": 0,
						"policies_rejected": 0,
						"snapshots_total": 0,
					},
				}
			)

	total_apps = len(apps)
	total_score = sum(int(x.get("compliance_score", 0) or 0) for x in apps)
	return {
		"apps": apps,
		"summary": {
			"apps_count": total_apps,
			"average_compliance_score": int(total_score / total_apps) if total_apps else 0,
			"policies_total": sum(int((x.get("governance") or {}).get("policies_total", 0) or 0) for x in apps),
			"policies_pending": sum(int((x.get("governance") or {}).get("policies_pending", 0) or 0) for x in apps),
			"snapshots_total": sum(int((x.get("governance") or {}).get("snapshots_total", 0) or 0) for x in apps),
		},
	}
