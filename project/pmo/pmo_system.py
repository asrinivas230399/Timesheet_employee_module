# Simulated PMO management system
def get_real_time_user_data():
    # This function simulates fetching real-time user data from a PMO system
    return [
        {"user_id": 1, "name": "Alice", "role": "Admin", "access_level": "High"},
        {"user_id": 2, "name": "Bob", "role": "User", "access_level": "Medium"},
        {"user_id": 3, "name": "Charlie", "role": "Guest", "access_level": "Low"},
        {"user_id": 4, "name": "David", "role": "Finance", "access_level": "High"},
    ]

def get_real_time_cost_data():
    # This function simulates fetching real-time cost data from a PMO system
    return {
        1: {"hourly_rate": 55, "employment_terms": "Full-time"},
        2: {"hourly_rate": 35, "employment_terms": "Part-time"},
        3: {"hourly_rate": 25, "employment_terms": "Contract"},
        4: {"hourly_rate": 65, "employment_terms": "Full-time"},
    }