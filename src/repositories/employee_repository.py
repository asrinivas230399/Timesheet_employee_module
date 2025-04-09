from sqlalchemy.orm import Session
from ..models import Employee
from ..schemas import EmployeeCreate
from ..utils import encrypt_data
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_employee(db: Session, employee: EmployeeCreate) -> Employee:
    """
    Business logic to add a new employee to the database.

    :param db: Database session
    :param employee: EmployeeCreate schema with employee details
    :return: The newly created Employee object
    """
    try:
        # Validate input data
        employee_data = employee.dict()
        
        # Encrypt sensitive information
        if 'name' in employee_data:
            employee_data['name'] = encrypt_data(employee_data['name'])

        db_employee = Employee(**employee_data)
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)

        # Log the addition of a new employee
        logger.info(f"Added new employee: {db_employee}")

        return db_employee
    except ValidationError as e:
        raise ValueError(f"Invalid data: {e}")