from src.models.role import Role

class Employee:
    def __init__(self, employee_id, name, contact_details, role, project_assignments):
        self.employee_id = employee_id
        self.name = name
        self.contact_details = contact_details
        self.role = role  # This should be an instance of Role
        self.project_assignments = project_assignments

    def update_role(self, new_role):
        if isinstance(new_role, Role):
            self.role = new_role
            print(f"Role updated to {self.role}")
        else:
            print("Invalid role provided")

    def update_project_assignments(self, new_project_assignments):
        self.project_assignments = new_project_assignments
        print(f"Project assignments updated to {self.project_assignments}")