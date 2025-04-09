from pydantic import BaseModel, EmailStr, ValidationError
from typing import Tuple, Union

class EmployeeData(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    position: str


def validate_employee_data(employee_data: dict) -> Tuple[bool, Union[str, None]]:
    """
    Validates the employee data.

    :param employee_data: A dictionary containing employee data.
    :return: A tuple where the first element is a boolean indicating if the data is valid,
             and the second element is an error message if the data is invalid.
    """
    try:
        EmployeeData(**employee_data)
        return True, None
    except ValidationError as e:
        return False, str(e)