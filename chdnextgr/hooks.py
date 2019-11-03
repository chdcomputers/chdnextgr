# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "chdnextgr"
app_title = "ChD ERP Next Greek support"
app_publisher = "ChD Computers"
app_description = "Greek country support for ERP Next"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "chdcomputers@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/chdnextgr/css/chdnextgr.css"
# app_include_js = "/assets/chdnextgr/js/chdnextgr.js"

# include js, css files in header of web template
# web_include_css = "/assets/chdnextgr/css/chdnextgr.css"
# web_include_js = "/assets/chdnextgr/js/chdnextgr.js"

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
# get_website_user_home_page = "chdnextgr.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "chdnextgr.install.before_install"
# after_install = "chdnextgr.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "chdnextgr.notifications.get_notification_config"

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
# 		"chdnextgr.tasks.all"
# 	],
# 	"daily": [
# 		"chdnextgr.tasks.daily"
# 	],
# 	"hourly": [
# 		"chdnextgr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"chdnextgr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"chdnextgr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "chdnextgr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "chdnextgr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "chdnextgr.task.get_dashboard_data"
# }
fixtures = ["Custom Field"]
