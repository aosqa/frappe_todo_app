// Copyright (c) 2026, Abduselam M and contributors
// For license information, please see license.txt

frappe.ui.form.on("Simple ToDo", {
    refresh(frm) {
        // Add a custom button to mark the task as Completed instantly
        if (frm.doc.status !== "Completed" && !frm.is_new()) {
            frm.add_custom_button(__("Mark as Completed"), () => {
                frm.set_value("status", "Completed");
                frm.save();
            }).addClass("btn-primary");
        }
    },
    
    status(frm) {
        // Triggered when status field changes
        if (frm.doc.status === "Completed") {
            frappe.show_alert({
                message: __("Great job completing this task!"),
                indicator: "green"
            });
        }
    }
});