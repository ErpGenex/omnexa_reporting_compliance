from __future__ import annotations

import frappe
from frappe.model.document import Document


class ComplianceControlTest(Document):
	def validate(self):
		if self.control and not frappe.db.exists("Compliance Control", self.control):
			frappe.throw(frappe._("Invalid Control."))

