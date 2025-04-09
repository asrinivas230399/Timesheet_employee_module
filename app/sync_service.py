import logging
from sqlalchemy.orm import Session
import httpx  # For asynchronous HTTP requests
from .models import SomeModel

class SyncService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def fetch_employee_roles(self):
        self.log_info("Fetching employee roles from the database.")
        try:
            return self.db_session.query(SomeModel).filter(SomeModel.type == 'role').all()
        except Exception as e:
            self.log_error(f"Error fetching employee roles: {e}")
            return []

    def fetch_project_assignments(self):
        self.log_info("Fetching project assignments from the database.")
        try:
            return self.db_session.query(SomeModel).filter(SomeModel.type == 'assignment').all()
        except Exception as e:
            self.log_error(f"Error fetching project assignments: {e}")
            return []

    def validate_data_integrity(self, roles, assignments):
        self.log_info("Validating data integrity.")
        if not roles or not assignments:
            self.log_error("Data integrity check failed: Roles or assignments are missing.")
            raise ValueError("Data integrity check failed: Roles or assignments are missing.")

    async def update_project_management_tool(self, data):
        self.log_info(f"Updating project management tool with data: {data}")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post("https://api.projectmanagementtool.com/update", json=data)
                response.raise_for_status()
                self.log_info(f"Project management tool updated successfully with status code: {response.status_code}")
                return response.status_code
        except httpx.RequestError as e:
            self.log_error(f"Error updating project management tool: {e}")
            return None

    async def synchronize(self):
        try:
            employee_roles = self.fetch_employee_roles()
            project_assignments = self.fetch_project_assignments()
            self.validate_data_integrity(employee_roles, project_assignments)
            data = {"roles": employee_roles, "assignments": project_assignments}
            status_code = await self.update_project_management_tool(data)
            if status_code is None:
                self.log_error("Synchronization failed due to an error in updating the project management tool.")
            else:
                self.log_info(f"Synchronization successful with status code: {status_code}")

        except ValueError as ve:
            self.log_error(f"Data integrity error: {ve}")
        except Exception as e:
            self.log_error(f"An unexpected error occurred during synchronization: {e}")

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)
