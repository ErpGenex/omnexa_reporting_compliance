# Copyright (c) 2026, ErpGenEx
from frappe.tests.utils import FrappeTestCase

from omnexa_core.omnexa_core.grc_parity import preview_grc


class TestSapParityGrcApp(FrappeTestCase):
	def test_grc_kpi(self):
		out = preview_grc("reporting_compliance", controls_total=10, controls_effective=9)
		self.assertEqual(out["kpi"]["control_coverage"], 0.9)
