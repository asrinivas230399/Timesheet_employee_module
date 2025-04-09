from functools import lru_cache

@lru_cache(maxsize=1)
def fetch_employee_data():
    return [
        {'id': 1, 'name': 'Alice Smith', 'position': 'Developer', 'status': 'Active', 'projects': ['Project A', 'Project B'], 'workday_duration': 8, 'hourly_rate': 50},
        {'id': 2, 'name': 'Bob Johnson', 'position': 'Designer', 'status': 'Inactive', 'projects': ['Project C'], 'workday_duration': 7, 'hourly_rate': 40},
        {'id': 3, 'name': 'Charlie Brown', 'position': 'Manager', 'status': 'Active', 'projects': ['Project D', 'Project E'], 'workday_duration': 9, 'hourly_rate': 60},
    ]
