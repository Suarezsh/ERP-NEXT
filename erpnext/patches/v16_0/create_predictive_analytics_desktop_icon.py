import frappe


def execute():
	"""Create Module Def and Desktop Icon for Predictive Analytics module."""
	
	# Ensure Module Def exists
	if not frappe.db.exists("Module Def", "Predictive Analytics"):
		module_def = frappe.new_doc("Module Def")
		module_def.module_name = "Predictive Analytics"
		module_def.app_name = "erpnext"
		module_def.insert(ignore_permissions=True)
	
	# Ensure Desktop Icon exists so the module appears in the sidebar
	if not frappe.db.exists("Desktop Icon", "Predictive Analytics"):
		desktop_icon = frappe.new_doc("Desktop Icon")
		desktop_icon.label = "Predictive Analytics"
		desktop_icon.icon = "organization"
		desktop_icon.icon_type = "External"
		desktop_icon.link = "/app/Predictive Analytics"
		desktop_icon.standard = 1
		desktop_icon.app = "erpnext"
		desktop_icon.idx = -1
		desktop_icon.insert(ignore_permissions=True)
