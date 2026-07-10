# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestProductPrediction(FrappeTestCase):
	def test_create_product_prediction(self):
		prediction = frappe.new_doc("Product Prediction")
		prediction.item = "_Test Item"
		prediction.prediction_date = frappe.utils.today()
		prediction.predicted_quantity = 100
		prediction.suggested_purchase_quantity = 50
		prediction.insert()
		self.assertIsNotNone(prediction.name)
		self.assertGreaterEqual(float(prediction.predicted_quantity), 0)
