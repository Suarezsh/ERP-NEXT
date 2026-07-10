# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

from datetime import date

from frappe.tests.utils import FrappeTestCase

from erpnext.predictive_analytics.utils import calculate_stockout_and_suggestion


class TestPredictiveAnalyticsUtils(FrappeTestCase):
	def test_calculate_stockout_and_suggestion(self):
		predictions = [
			{"date": date(2026, 7, 11), "predicted_quantity": 10},
			{"date": date(2026, 7, 12), "predicted_quantity": 15},
			{"date": date(2026, 7, 13), "predicted_quantity": 20},
		]

		result = calculate_stockout_and_suggestion(
			current_stock=30,
			predictions=predictions,
			safety_stock_days=2,
			avg_daily_sales=10,
		)

		self.assertEqual(result["stockout_date"], date(2026, 7, 12))
		self.assertEqual(result["suggested_purchase_quantity"], 35.0)

	def test_suggested_purchase_never_negative(self):
		predictions = [
			{"date": date(2026, 7, 11), "predicted_quantity": 5},
		]

		result = calculate_stockout_and_suggestion(
			current_stock=100,
			predictions=predictions,
			safety_stock_days=1,
			avg_daily_sales=10,
		)

		self.assertEqual(result["suggested_purchase_quantity"], 0.0)
