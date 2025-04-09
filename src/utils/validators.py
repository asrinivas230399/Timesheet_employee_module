class Validators:
    @staticmethod
    def validate_employee_data(employee_data):
        if not employee_data.get('employee_id'):
            return "Employee ID is required."
        if not employee_data.get('name'):
            return "Employee name is required."
        if not employee_data.get('contact_details'):
            return "Contact details are required."
        if not employee_data.get('role') or not isinstance(employee_data['role'], dict):
            return "Valid role information is required."
        if not employee_data.get('project_assignments') or not isinstance(employee_data['project_assignments'], list):
            return "Valid project assignments are required."
        return None

    @staticmethod
    def validate_role_data(role_data):
        if not role_data.get('role_id'):
            return "Role ID is required."
        if not role_data.get('role_name'):
            return "Role name is required."
        return None

    @staticmethod
    def validate_project_data(project_data):
        if not project_data.get('project_id'):
            return "Project ID is required."
        if not project_data.get('project_name'):
            return "Project name is required."
        return None