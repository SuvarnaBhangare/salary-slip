# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hr_salary_slip"
app_title = "Hr Salary Slip"
app_publisher = "info@progressiveit.in"
app_description = "salary Slip calculations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pranali@progressiveit.in"
app_license = "MIT"



fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hr_salary_slip/css/hr_salary_slip.css"
# app_include_js = "/assets/hr_salary_slip/js/hr_salary_slip.js"

# include js, css files in header of web template
# web_include_css = "/assets/hr_salary_slip/css/hr_salary_slip.css"
# web_include_js = "/assets/hr_salary_slip/js/hr_salary_slip.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hr_salary_slip.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hr_salary_slip.install.before_install"
# after_install = "hr_salary_slip.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hr_salary_slip.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events



doc_events = {
	"Salary Slip": {
		"validate": ["hr_salary_slip.hr_salary_slip.salary_slip_custom.calculate_privilege_leave","hr_salary_slip.hr_salary_slip.salary_slip_custom.calculate_casual_leave",
                "hr_salary_slip.hr_salary_slip.salary_slip_custom.calculate_sick_leave" ]
		
		
	}
}
    


# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hr_salary_slip.tasks.all"
# 	],
# 	"daily": [
# 		"hr_salary_slip.tasks.daily"
# 	],
# 	"hourly": [
# 		"hr_salary_slip.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hr_salary_slip.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hr_salary_slip.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hr_salary_slip.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hr_salary_slip.event.get_events"
# }

