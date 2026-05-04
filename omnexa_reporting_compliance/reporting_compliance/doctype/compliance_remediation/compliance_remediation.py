from __future__ import annotations

import frappe
from frappe.model.document import Document


class ComplianceRemediation(Document):
	def validate(self):
		if self.exception and not frappe.db.exists("Compliance Exception", self.exception):
			frappe.throw(frappe._("Invalid Exception."))

