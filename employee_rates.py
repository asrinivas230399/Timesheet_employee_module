from .role_based_access import is_authorized, check_access

def get_hourly_rate(employee_id, role):
    # Check if the user is authorized
    if not check_access(role, 'view_budget'):
        raise PermissionError("Access denied. You are not authorized to view employee rates.")

    # Mock data for hourly rates
    hourly_rates = {
        1: 50.0,
        2: 60.0,
        3: 55.0,
    }
    return hourly_rates.get(employee_id, 0.0)
