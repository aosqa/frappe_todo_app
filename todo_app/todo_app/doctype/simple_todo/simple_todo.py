# Copyright (c) 2026, Abduselam M and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime, getdate, today
from frappe import _
class SimpleToDo(Document):
    
    def validate(self):
        # Automatically set or clear completion time based on status
        if self.status == "Completed" and not self.get("completed_at"):
            self.completed_at = now_datetime()
        elif self.status != "Completed":
            self.completed_at = None
        if self.due_date and getdate(self.due_date) < getdate(today()):
            frappe.throw(_("Due date cannot be set in the past."))

    @frappe.whitelist()
    def mark_complete(self):
        """Server-side method callable via REST API or client script"""
        self.status = "Completed"
        self.completed_at = now_datetime()
        self.save()
        frappe.msgprint(_("Task marked as complete successfully!"))

    def get_indicator(self):
        """Define custom color indicators for list view"""
        if self.status == "Completed":
            return "green"
        elif self.status == "InProgress":
            return "blue"
        elif self.priority == "High":
            return "red"
        else:
            return "orange"