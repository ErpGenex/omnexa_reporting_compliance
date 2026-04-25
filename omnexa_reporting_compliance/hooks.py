app_name = "omnexa_reporting_compliance"
app_title = "ErpGenEx — Reporting Compliance"
app_publisher = "ErpGenEx"
app_description = "Shared reporting and compliance services"
app_email = "dev@erpgenex.com"
app_license = "mit"

# Apps
# ------------------

required_apps = ["omnexa_core"]

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "omnexa_reporting_compliance",
		"logo": "/assets/omnexa_reporting_compliance/logo.png",
		"title": "Omnexa Reporting Compliance",
		"route": "/app/compliance-control",
		"has_permission": "omnexa_reporting_compliance.permission.has_app_permission",
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/omnexa_reporting_compliance/css/omnexa_reporting_compliance.css"
# app_include_js = "/assets/omnexa_reporting_compliance/js/omnexa_reporting_compliance.js"

# include js, css files in header of web template
# web_include_css = "/assets/omnexa_reporting_compliance/css/omnexa_reporting_compliance.css"
# web_include_js = "/assets/omnexa_reporting_compliance/js/omnexa_reporting_compliance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "omnexa_reporting_compliance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "omnexa_reporting_compliance/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "omnexa_reporting_compliance.utils.jinja_methods",
# 	"filters": "omnexa_reporting_compliance.utils.jinja_filters"
# }

# Installation
# ------------

before_install = "omnexa_reporting_compliance.install.enforce_supported_frappe_version"
before_migrate = "omnexa_reporting_compliance.install.enforce_supported_frappe_version"
after_migrate = "omnexa_reporting_compliance.install.after_migrate"

# Uninstallation
# ------------

# before_uninstall = "omnexa_reporting_compliance.uninstall.before_uninstall"
# after_uninstall = "omnexa_reporting_compliance.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "omnexa_reporting_compliance.utils.before_app_install"
# after_app_install = "omnexa_reporting_compliance.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "omnexa_reporting_compliance.utils.before_app_uninstall"
# after_app_uninstall = "omnexa_reporting_compliance.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "omnexa_reporting_compliance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
has_permission = {
	"Compliance Control": "omnexa_reporting_compliance.permission.has_doctype_permission",
	"Compliance Control Test": "omnexa_reporting_compliance.permission.has_doctype_permission",
	"Compliance Exception": "omnexa_reporting_compliance.permission.has_doctype_permission",
	"Compliance Remediation": "omnexa_reporting_compliance.permission.has_doctype_permission",
	"Compliance Evidence": "omnexa_reporting_compliance.permission.has_doctype_permission",
}

permission_query_conditions = {
	"Compliance Control": "omnexa_reporting_compliance.permission.get_doctype_permission_query_conditions",
	"Compliance Control Test": "omnexa_reporting_compliance.permission.get_doctype_permission_query_conditions",
	"Compliance Exception": "omnexa_reporting_compliance.permission.get_doctype_permission_query_conditions",
	"Compliance Remediation": "omnexa_reporting_compliance.permission.get_doctype_permission_query_conditions",
	"Compliance Evidence": "omnexa_reporting_compliance.permission.get_doctype_permission_query_conditions",
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"omnexa_reporting_compliance.tasks.all"
# 	],
# 	"daily": [
# 		"omnexa_reporting_compliance.tasks.daily"
# 	],
# 	"hourly": [
# 		"omnexa_reporting_compliance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"omnexa_reporting_compliance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"omnexa_reporting_compliance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "omnexa_reporting_compliance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "omnexa_reporting_compliance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "omnexa_reporting_compliance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
before_request = [
	"omnexa_reporting_compliance.permission.before_request",
	"omnexa_reporting_compliance.license_gate.before_request",
]
# after_request = ["omnexa_reporting_compliance.utils.after_request"]

# Job Events
# ----------
# before_job = ["omnexa_reporting_compliance.utils.before_job"]
# after_job = ["omnexa_reporting_compliance.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"omnexa_reporting_compliance.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

