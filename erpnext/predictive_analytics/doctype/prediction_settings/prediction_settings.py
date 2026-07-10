# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

from frappe.model.document import Document


class PredictionSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		default_prediction_days: DF.Int
		default_warehouse: DF.Link | None
		enable_predictions: DF.Check
		minimum_history_days: DF.Int
		model_type: DF.Literal["Random Forest", "Linear Regression"]
		safety_stock_days: DF.Int
	# end: auto-generated types

	pass
