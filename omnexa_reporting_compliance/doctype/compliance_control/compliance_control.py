from __future__ import annotations

import frappe
from frappe.model.document import Document


class ComplianceControl(Document):
	def validate(self):
		if self.company and not frappe.db.exists("Company", self.company):
			frappe.throw(frappe._("Invalid Company."))

