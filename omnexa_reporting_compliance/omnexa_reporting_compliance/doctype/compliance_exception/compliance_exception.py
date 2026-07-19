from __future__ import annotations

import frappe
from frappe.model.document import Document


class ComplianceException(Document):
	def validate(self):
		if self.control and not frappe.db.exists("Compliance Control", self.control):
			frappe.throw(frappe._("Invalid Control."))
		if self.control_test and not frappe.db.exists("Compliance Control Test", self.control_test):
			frappe.throw(frappe._("Invalid Control Test."))

