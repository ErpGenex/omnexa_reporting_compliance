from __future__ import annotations

from urllib.parse import unquote

import frappe

_DEFAULT_ALLOWED_ROLES = frozenset(
	{
		"System Manager",
		"Compliance Manager",
		"General Manager",
		"Audit Supervisor",
		"مدير الامتثال",
		"المدير العام",
		"مراقب الحسابات",
	}
)

_COMPLIANCE_DOCTYPES = frozenset(
	{
		"Compliance Control",
		"Compliance Control Test",
		"Compliance Exception",
		"Compliance Remediation",
		"Compliance Evidence",
	}
)


def _allowed_roles() -> set[str]:
	raw = frappe.conf.get("omnexa_reporting_compliance_allowed_roles")
	if isinstance(raw, str) and raw.strip():
		return {r.strip() for r in raw.split(",") if r.strip()}
	if isinstance(raw, (list, tuple, set)):
		return {str(r).strip() for r in raw if str(r).strip()}
	return set(_DEFAULT_ALLOWED_ROLES)


def has_compliance_access(user: str | None = None) -> bool:
	user = user or frappe.session.user
	if not user or user == "Guest":
		return False
	if user == "Administrator":
		return True
	roles = set(frappe.get_roles(user) or [])
	return bool(roles.intersection(_allowed_roles()))


def assert_compliance_access(user: str | None = None) -> None:
	if has_compliance_access(user=user):
		return
	frappe.throw(
		frappe._("Access denied. You do not have access to Reporting Compliance."),
		frappe.PermissionError,
	)


def has_app_permission() -> bool:
	return has_compliance_access()


def has_doctype_permission(doc=None, user: str | None = None, permission_type: str | None = None) -> bool:
	return has_compliance_access(user=user)


def get_doctype_permission_query_conditions(user: str | None = None) -> str | None:
	if has_compliance_access(user=user):
		return None
	return "1=0"


def before_request() -> None:
	"""Guard app and resource paths for non-authorized users."""
	if not getattr(frappe.local, "request", None):
		return
	path = (frappe.local.request.path or "").strip()
	if not path:
		return
	for prefix in ("/assets/", "/files/", "/.well-known"):
		if path.startswith(prefix):
			return
	if has_compliance_access():
		return
	if path.startswith("/app/compliance"):
		assert_compliance_access()
	if path.startswith("/api/method/omnexa_reporting_compliance."):
		assert_compliance_access()
	if path.startswith("/api/resource/"):
		resource = unquote(path[len("/api/resource/") :]).split("/", 1)[0].strip()
		if resource in _COMPLIANCE_DOCTYPES:
			assert_compliance_access()

