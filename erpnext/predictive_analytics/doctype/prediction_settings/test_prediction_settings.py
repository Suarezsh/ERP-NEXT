# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestPredictionSettings(FrappeTestCase):
	def test_default_values(self):
		settings = frappe.get_doc("Prediction Settings")
		self.assertTrue(settings.enable_predictions)
		self.assertEqual(settings.default_prediction_days, 30)
		self.assertEqual(settings.minimum_history_days, 60)
		self.assertEqual(settings.safety_stock_days, 7)
