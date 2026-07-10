# Copyright (c) 2026, Suarezsh and contributors
# License: GNU General Public License v3. See license.txt

from __future__ import annotations

from collections import defaultdict
from datetime import date, datetime, timedelta
from typing import Any

import frappe
from frappe.utils import add_days, cint, flt, getdate, now


# Lazy imports so the module loads even when ML libraries are not installed yet.
# Install them with: bench pip install scikit-learn pandas
sklearn = None
np = None
pd = None
LinearRegression = None
RandomForestRegressor = None


def _import_ml_libraries():
	"""Import optional ML libraries and return them as a tuple."""
	global sklearn, np, pd, LinearRegression, RandomForestRegressor
	if sklearn is None:
		import numpy as np  # noqa: F401
		import pandas as pd  # noqa: F401
		from sklearn.ensemble import RandomForestRegressor  # noqa: F401
		from sklearn.linear_model import LinearRegression  # noqa: F401
		import sklearn  # noqa: F401

	return np, pd, LinearRegression, RandomForestRegressor


def get_sales_history(item_code: str, from_date: date | None = None, to_date: date | None = None) -> list[dict]:
	"""Return daily sales quantity for an item from submitted Sales Invoices."""
	conditions = ["si.docstatus = 1", "sii.item_code = %s"]
	values = [item_code]

	if from_date:
		conditions.append("si.posting_date >= %s")
		values.append(from_date)

	if to_date:
		conditions.append("si.posting_date <= %s")
		values.append(to_date)

	query = f"""
		SELECT
			si.posting_date AS posting_date,
			SUM(sii.qty) AS qty
		FROM `tabSales Invoice` si
		INNER JOIN `tabSales Invoice Item` sii ON sii.parent = si.name
		WHERE {' AND '.join(conditions)}
		GROUP BY si.posting_date
		ORDER BY si.posting_date ASC
	"""

	return frappe.db.sql(query, tuple(values), as_dict=True)


def get_item_stock(item_code: str, warehouse: str | None = None) -> float:
	"""Return current stock quantity for an item."""
	filters = {"item_code": item_code, "is_cancelled": 0}
	if warehouse:
		filters["warehouse"] = warehouse

	qty = frappe.db.get_value("Bin", filters, "sum(actual_qty)")
	return flt(qty)


def get_active_items() -> list[str]:
	"""Return list of item codes that have sales history."""
	return frappe.db.sql_list(
		"""
		SELECT DISTINCT sii.item_code
		FROM `tabSales Invoice Item` sii
		INNER JOIN `tabSales Invoice` si ON si.name = sii.parent
		WHERE si.docstatus = 1
	"""
	)


def build_features(dates: list[date], quantities: list[float]) -> tuple[Any, Any]:
	"""Convert dates into numeric features suitable for regression models."""
	np, pd, _, _ = _import_ml_libraries()

	data = pd.DataFrame({
		"date": dates,
		"qty": quantities,
	})
	data["dayofweek"] = data["date"].apply(lambda d: d.weekday())
	data["month"] = data["date"].apply(lambda d: d.month)
	data["day"] = data["date"].apply(lambda d: d.day)
	data["is_weekend"] = data["dayofweek"].apply(lambda x: 1 if x >= 5 else 0)
	data["days_since_start"] = (data["date"] - data["date"].min()).apply(lambda x: x.days)

	X = data[["dayofweek", "month", "day", "is_weekend", "days_since_start"]].values
	y = data["qty"].values

	return X, y


def train_model(X: Any, y: Any, model_type: str = "Random Forest") -> Any:
	"""Train a regression model on the provided features."""
	np, pd, LinearRegression, RandomForestRegressor = _import_ml_libraries()

	if model_type == "Linear Regression":
		model = LinearRegression()
	else:
		# Use a small forest so it trains quickly even with limited data.
		n_estimators = min(100, max(10, len(y)))
		model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)

	model.fit(X, y)
	return model


def predict_future(
	model: Any,
	last_date: date,
	prediction_days: int,
	historical_dates: list[date],
) -> list[dict]:
	"""Generate daily predictions for the next N days."""
	np, pd, _, _ = _import_ml_libraries()

	start_date = add_days(last_date, 1)
	predictions = []
	start_ref = min(historical_dates)

	for i in range(prediction_days):
		d = getdate(add_days(start_date, i))
		days_since_start = (d - start_ref).days
		features = [[d.weekday(), d.month, d.day, 1 if d.weekday() >= 5 else 0, days_since_start]]
		pred = max(0.0, float(model.predict(features)[0]))
		predictions.append({
			"date": d,
			"predicted_quantity": pred,
		})

	return predictions


def calculate_stockout_and_suggestion(
	current_stock: float,
	predictions: list[dict],
	safety_stock_days: int,
	avg_daily_sales: float,
) -> dict:
	"""Estimate stockout date and suggested purchase quantity."""
	remaining = current_stock
	stockout_date = None
	cumulative_predicted = 0.0

	for day in predictions:
		cumulative_predicted += day["predicted_quantity"]
		remaining -= day["predicted_quantity"]
		if stockout_date is None and remaining <= 0:
			stockout_date = day["date"]

	# Suggested purchase = predicted demand during period + safety buffer.
	safety_buffer = safety_stock_days * avg_daily_sales
	suggested_qty = cumulative_predicted + safety_buffer - current_stock
	suggested_qty = max(0.0, suggested_qty)

	return {
		"stockout_date": stockout_date,
		"suggested_purchase_quantity": round(suggested_qty, 2),
	}


def run_prediction_for_item(
	item_code: str,
	prediction_days: int = 30,
	model_type: str = "Random Forest",
	safety_stock_days: int = 7,
	warehouse: str | None = None,
	min_history_days: int = 14,
) -> dict | None:
	"""Run the full prediction pipeline for a single item."""
	history = get_sales_history(item_code)

	if len(history) < min_history_days:
		# Not enough history to build a reliable model.
		return None

	dates = [getdate(row.posting_date) for row in history]
	quantities = [flt(row.qty) for row in history]

	# Aggregate by date just in case the query returned duplicates.
	daily: dict[date, float] = defaultdict(float)
	for d, q in zip(dates, quantities):
		daily[d] += q

	dates = sorted(daily.keys())
	quantities = [daily[d] for d in dates]

	if len(dates) < min_history_days:
		return None

	try:
		X, y = build_features(dates, quantities)
		model = train_model(X, y, model_type)
		predictions = predict_future(model, dates[-1], prediction_days, dates)
	except Exception:
		frappe.log_error(title="Predictive Analytics Error")
		return None

	current_stock = get_item_stock(item_code, warehouse)
	avg_daily_sales = sum(quantities) / max(1, len(quantities))

	extras = calculate_stockout_and_suggestion(
		current_stock, predictions, safety_stock_days, avg_daily_sales
	)

	total_predicted = sum(p["predicted_quantity"] for p in predictions)

	return {
		"item": item_code,
		"warehouse": warehouse,
		"current_stock": current_stock,
		"avg_daily_sales": round(avg_daily_sales, 2),
		"predicted_total": round(total_predicted, 2),
		"predicted_daily": predictions,
		"stockout_date": extras["stockout_date"],
		"suggested_purchase_quantity": extras["suggested_purchase_quantity"],
	}


@frappe.whitelist()
def generate_predictions(prediction_run_name: str | None = None) -> dict:
	"""Main entry point: generate predictions for all active items."""
	settings = frappe.get_doc("Prediction Settings")

	if not settings.enable_predictions:
		frappe.throw("Predictions are disabled in Prediction Settings.")

	if prediction_run_name:
		run = frappe.get_doc("Prediction Run", prediction_run_name)
	else:
		run = frappe.new_doc("Prediction Run")
		run.run_date = now()
		run.prediction_period_days = settings.default_prediction_days
		run.status = "Draft"
		run.insert()

	run.status = "Running"
	run.model_used = settings.model_type
	run.from_date = add_days(getdate(), -cint(settings.minimum_history_days))
	run.to_date = getdate()
	run.save(ignore_permissions=True)
	frappe.db.commit()

	items = get_active_items()
	run.total_products = len(items)
	run.processed_products = 0
	run.save(ignore_permissions=True)
	frappe.db.commit()

	processed = 0
	errors = []

	for item_code in items:
		try:
			result = run_prediction_for_item(
				item_code=item_code,
				prediction_days=cint(run.prediction_period_days),
				model_type=settings.model_type,
				safety_stock_days=cint(settings.safety_stock_days),
				warehouse=settings.default_warehouse,
				min_history_days=cint(settings.minimum_history_days),
			)

			if not result:
				continue

			# Save a summary prediction for the whole period.
			prediction = frappe.new_doc("Product Prediction")
			prediction.item = item_code
			prediction.item_name = frappe.db.get_value("Item", item_code, "item_name")
			prediction.prediction_run = run.name
			prediction.prediction_date = add_days(getdate(), run.prediction_period_days)
			prediction.warehouse = settings.default_warehouse
			prediction.predicted_quantity = result["predicted_total"]
			prediction.current_stock = result["current_stock"]
			prediction.stockout_date = result["stockout_date"]
			prediction.suggested_purchase_quantity = result["suggested_purchase_quantity"]
			prediction.insert(ignore_permissions=True)

		except Exception as e:
			errors.append(f"{item_code}: {str(e)}")
			frappe.log_error(title=f"Prediction failed for {item_code}")

		processed += 1
		run.processed_products = processed
		run.save(ignore_permissions=True)
		frappe.db.commit()

	if errors:
		run.status = "Failed"
		run.error_log = "\n".join(errors)
	else:
		run.status = "Completed"

	run.save(ignore_permissions=True)
	frappe.db.commit()

	return {"run": run.name, "processed": processed, "errors": errors}
