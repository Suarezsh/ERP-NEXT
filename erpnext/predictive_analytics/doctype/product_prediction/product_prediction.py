# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

from frappe.model.document import Document


class ProductPrediction(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_quantity: DF.Float
		confidence_score: DF.Percent
		current_stock: DF.Float
		item: DF.Link
		item_name: DF.Data | None
		predicted_quantity: DF.Float
		prediction_date: DF.Date
		prediction_run: DF.Link | None
		stockout_date: DF.Date | None
		suggested_purchase_quantity: DF.Float
		warehouse: DF.Link | None
	# end: auto-generated types

	pass
