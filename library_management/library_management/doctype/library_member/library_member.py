# Copyright (c)  2021, Shabna Sherin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LIbraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
class LibraryMembership(Document):
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,      
                "docstatus": 1,                
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")