# WeeklyTimesheet Navigation Configuration
# This file defines the navigation structure for the WeeklyTimesheet module

from frappe import _

def get_data():
    """Return navigation data for WeeklyTimesheet module"""

    return [
        {
            "label": _("Weekly Timesheet"),
            "icon": "octicon octicon-calendar",
            "items": [
                {
                    "type": "doctype",
                    "name": "WeeklyTimesheet",
                    "label": _("Weekly Timesheet"),
                    "description": _("Manage weekly timesheets"),
                    "route": "/app/weeklytimesheet"
                },
                {
                    "type": "page",
                    "name": "timesheet-dashboard",
                    "label": _("Dashboard"),
                    "description": _("Timesheet Dashboard"),
                    "route": "/timesheet_dashboard"
                }
            ]
        }
    ]
