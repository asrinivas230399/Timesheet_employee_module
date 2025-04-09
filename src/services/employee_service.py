from src.models.employee import Employee
from src.models.role import Role
from src.models.project import Project
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmployeeService:
    def __init__(self):
        self.employees = []  # This will store Employee objects

    def add_employee(self, employee_id, name, contact_details, role, project_assignments):
        if not isinstance(role, Role):
            logging.error("Invalid role provided")
            return
        new_employee = Employee(employee_id, name, contact_details, role, project_assignments)
        self.employees.append(new_employee)
        logging.info(f"Added new employee: {new_employee.name}")

    def update_employee_role(self, employee_id, new_role):
        if not isinstance(new_role, Role):
            logging.error("Invalid role provided")
            return
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.update_role(new_role)
                logging.info(f"Updated role for employee {employee.name} to {new_role}")
                return
        logging.warning(f"Employee with ID {employee_id} not found")

    def assign_projects_to_employee(self, employee_id, new_project_assignments):
        if not all(isinstance(project, Project) for project in new_project_assignments):
            logging.error("Invalid project assignments provided")
            return
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.update_project_assignments(new_project_assignments)
                logging.info(f"Updated project assignments for employee {employee.name}")
                return
        logging.warning(f"Employee with ID {employee_id} not found")