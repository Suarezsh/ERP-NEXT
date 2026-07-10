# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe.model.document import Document


class PredictionRun(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		error_log: DF.Text | None
		from_date: DF.Date | None
		model_used: DF.Data | None
		prediction_period_days: DF.Int
		processed_products: DF.Int
		run_date: DF.Datetime
		status: DF.Literal["Draft", "Running", "Completed", "Failed"]
		to_date: DF.Date | None
		total_products: DF.Int
	# end: auto-generated types

	def on_submit(self):
		# In case the DocType is made submittable later, trigger generation.
		self.generate_predictions()

	@frappe.whitelist()
	def generate_predictions(self):
		from erpnext.predictive_analytics.utils import generate_predictions

		return generate_predictions(self.name)

	@frappe.whitelist()
	def generate_predictions_background(self):
		"""Enqueue prediction run in background to avoid request timeout."""
		frappe.enqueue(
			"erpnext.predictive_analytics.utils.generate_predictions",
			prediction_run_name=self.name,
			queue="long",
			timeout=3600,
		)
		return {"status": "queued", "run": self.name}
