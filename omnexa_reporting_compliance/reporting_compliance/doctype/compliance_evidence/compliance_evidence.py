from __future__ import annotations

import frappe
from frappe.model.document import Document


class ComplianceEvidence(Document):
	def validate(self):
		if self.control and not frappe.db.exists("Compliance Control", self.control):
			frappe.throw(frappe._("Invalid Control."))
		if self.exception and not frappe.db.exists("Compliance Exception", self.exception):
			frappe.throw(frappe._("Invalid Exception."))
		if self.remediation and not frappe.db.exists("Compliance Remediation", self.remediation):
			frappe.throw(frappe._("Invalid Remediation."))

