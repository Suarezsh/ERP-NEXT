# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestPredictionRun(FrappeTestCase):
	def test_create_prediction_run(self):
		run = frappe.new_doc("Prediction Run")
		run.prediction_period_days = 30
		run.status = "Draft"
		run.insert()
		self.assertIsNotNone(run.name)
		self.assertEqual(run.status, "Draft")
