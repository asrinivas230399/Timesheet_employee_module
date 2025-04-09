# Employee Rates Module Documentation

## Overview
The `employee_rates.py` module is responsible for managing and retrieving hourly rates for employees. It includes role-based access control to ensure that only authorized users can view employee rates.

## Functions

### `get_hourly_rate(employee_id, role)`
- **Description**: Retrieves the hourly rate for a given employee ID.
- **Parameters**:
  - `employee_id` (int): The ID of the employee whose rate is to be retrieved.
  - `role` (str): The role of the user requesting the rate.
- **Returns**: The hourly rate for the employee if the user is authorized; otherwise, raises a `PermissionError`.
- **Authorization**: The function checks if the user is authorized to view employee rates using the `is_authorized()` function from the `role_based_access` module.

## Usage
1. **Authorization Check**: Ensure the user has the appropriate role to access employee rates.
2. **Retrieve Rate**: Call `get_hourly_rate()` with the employee ID and user role.

## Example
```python
from employee_rates import get_hourly_rate

try:
    rate = get_hourly_rate(1, 'finance_team')
    print(f"Hourly rate for employee 1: {rate}")
except PermissionError:
    print("Access denied. You are not authorized to view employee rates.")
```

## User Acceptance Testing
- **Objective**: Verify that the `get_hourly_rate()` function correctly enforces role-based access control and returns the correct hourly rate.
- **Test Cases**:
  1. **Authorized Access**: Test with a role that is authorized to view rates (e.g., `finance_team`).
  2. **Unauthorized Access**: Test with a role that is not authorized (e.g., `guest`) and expect a `PermissionError`.

## Feedback
Please provide feedback on the module's functionality and documentation to help us improve.