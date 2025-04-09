# employee_rates.py

def get_hourly_rate(employee_id):
    # Mock data for hourly rates
    hourly_rates = {
        1: 50.0,
        2: 60.0,
        3: 55.0,
    }
    return hourly_rates.get(employee_id, 0.0)
