from __future__ import unicode_literals
import frappe
from frappe import _
from erpnext.hr.doctype.leave_application.leave_application \
    import get_leave_allocation_records, get_leave_balance_on, get_approved_leaves_for_period


leave_types = frappe.db.sql_list("select name from `tabLeave Type` order by name asc")   
    


    
       
def calculate_privilege_leave( doc,method):
    user = frappe.session.user
    start_date=doc.start_date
    end_date=doc.end_date
    allocation_records_based_on_to_date = get_leave_allocation_records(end_date)
    employee_name=doc.employee_name



    active_employees = frappe.get_all("Employee", 
         
        fields = ["name", "employee_name", "department", "user_id"])
    a=0.0
    b=0.0
    t=0.0
    leaves_taken=0.0
    
    for employee in active_employees:
        leave_approvers = [l.leave_approver for l in frappe.db.sql("""select leave_approver from `tabEmployee Leave Approver` where parent = %s""",
                            (employee.name),as_dict=True)]
    
        if (len(leave_approvers) and user in leave_approvers) or (user in ["Administrator", employee.user_id]) or ("HR Manager" in frappe.get_roles(user)):
            

            
                # leaves taken
                leaves_taken = get_approved_leaves_for_period(employee.name,  "Privilege Leave",
                    start_date, end_date)
                a=a+leaves_taken;
    conditions = (" and employee_name='%s'" % employee_name)
    allocation_records = frappe.db.sql("""
        select total_leaves_allocated,from_date,to_date
        from `tabLeave Allocation`
        where leave_type="Privilege Leave" and docstatus=1 {0}""".format(conditions) ,as_list=1)


    salary_slip_list=frappe.db.sql("""
        select start_date,end_date,pending_leaves,casual_leaves,sick_leaves
        from `tabSalary Slip`
        where docstatus=1 {0}""".format(conditions) ,as_list=1)



    if len(salary_slip_list)!=0:
        length=len(salary_slip_list)
        t =frappe.utils.data.flt (salary_slip_list[length-1][2], precision=1)
        doc.pending_leaves=t-a;

    if len(salary_slip_list)==0:
        if allocation_records[0][1]<=start_date and start_date<=allocation_records[0][2]:
            doc.pending_leaves=allocation_records[0][0]-a;





def calculate_casual_leave( doc,method):
    user = frappe.session.user
    start_date=doc.start_date
    end_date=doc.end_date
    allocation_records_based_on_to_date = get_leave_allocation_records(end_date)
    employee_name=doc.employee_name



    active_employees = frappe.get_all("Employee", 
         
        fields = ["name", "employee_name", "department", "user_id"])
    a=0.0
    b=0.0
    t=0.0
    leaves_taken=0.0
    
    for employee in active_employees:
        leave_approvers = [l.leave_approver for l in frappe.db.sql("""select leave_approver from `tabEmployee Leave Approver` where parent = %s""",
                            (employee.name),as_dict=True)]
    
        if (len(leave_approvers) and user in leave_approvers) or (user in ["Administrator", employee.user_id]) or ("HR Manager" in frappe.get_roles(user)):
            

            
                # leaves taken
                leaves_taken = get_approved_leaves_for_period(employee.name,  "Casual Leave",
                    start_date, end_date)
                a=a+leaves_taken;
    conditions = (" and employee_name='%s'" % employee_name)
    allocation_records = frappe.db.sql("""
        select total_leaves_allocated,from_date,to_date
        from `tabLeave Allocation`
        where leave_type="Casual Leave" and docstatus=1 {0}""".format(conditions) ,as_list=1)


    salary_slip_list=frappe.db.sql("""
        select start_date,end_date,pending_leaves,casual_leaves,sick_leaves
        from `tabSalary Slip`
        where docstatus=1 {0}""".format(conditions) ,as_list=1)



    if len(salary_slip_list)!=0:
        length=len(salary_slip_list)
        t =frappe.utils.data.flt (salary_slip_list[length-1][3], precision=1)
        doc.casual_leaves=t-a;

    if len(salary_slip_list)==0:
        if allocation_records[0][1]<=start_date and start_date<=allocation_records[0][2]:
            doc.casual_leaves=allocation_records[0][0]-a;




def calculate_sick_leave( doc,method):
    user = frappe.session.user
    start_date=doc.start_date
    end_date=doc.end_date
    allocation_records_based_on_to_date = get_leave_allocation_records(end_date)
    employee_name=doc.employee_name



    active_employees = frappe.get_all("Employee", 
         
        fields = ["name", "employee_name", "department", "user_id"])
    a=0.0
    b=0.0
    t=0.0
    leaves_taken=0.0
    
    for employee in active_employees:
        leave_approvers = [l.leave_approver for l in frappe.db.sql("""select leave_approver from `tabEmployee Leave Approver` where parent = %s""",
                            (employee.name),as_dict=True)]
    
        if (len(leave_approvers) and user in leave_approvers) or (user in ["Administrator", employee.user_id]) or ("HR Manager" in frappe.get_roles(user)):
            

            
                # leaves taken
                leaves_taken = get_approved_leaves_for_period(employee.name,  "Sick Leave",
                    start_date, end_date)
                a=a+leaves_taken;
    conditions = (" and employee_name='%s'" % employee_name)
    allocation_records = frappe.db.sql("""
        select total_leaves_allocated,from_date,to_date
        from `tabLeave Allocation`
        where leave_type="Sick Leave" and docstatus=1 {0}""".format(conditions) ,as_list=1)


    salary_slip_list=frappe.db.sql("""
        select start_date,end_date,pending_leaves,casual_leaves,sick_leaves
        from `tabSalary Slip`
        where docstatus=1 {0}""".format(conditions) ,as_list=1)



    if len(salary_slip_list)!=0:
        length=len(salary_slip_list)
        t =frappe.utils.data.flt (salary_slip_list[length-1][4], precision=1)
        doc.sick_leaves=t-a;

    if len(salary_slip_list)==0:
        if allocation_records[0][1]<=start_date and start_date<=allocation_records[0][2]:
            doc.sick_leaves=allocation_records[0][0]-a;




