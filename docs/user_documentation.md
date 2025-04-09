# User Documentation for Budget Allocation System

## Overview
The Budget Allocation System is designed to help manage and track budget allocations for employees across different projects. It provides functionalities to view, filter, and update budget allocations, as well as generate alerts when budget thresholds are exceeded.

## Modules

### 1. `employee_rates.py`
- **Function:** `get_hourly_rate(employee_id)`
  - Retrieves the hourly rate for a given employee ID.

### 2. `budget_allocation.py`
- **Function:** `view_budget_allocations()`
  - Returns a list of budget allocations for employees, including details such as allocated hours, hourly rate, total cost, project, and date.
- **Function:** `filter_budget_data(employee_id=None, project=None, start_date=None, end_date=None)`
  - Filters budget allocations based on employee ID, project, and date range.
- **Function:** `update_budget_usage()`
  - Continuously updates and prints the current budget allocations every 60 seconds.
- **Function:** `generate_alerts(threshold)`
  - Generates alerts if the total cost for any allocation exceeds the specified threshold.

### 3. `role_based_access.py`
- **Function:** `is_authorized(role)`
  - Checks if a user is authorized based on their role.

### 4. `alert_system.py`
- **Function:** `send_alert(message)`
  - Sends an alert message.

## Usage
1. **Authorization**: Ensure the user is authorized by checking their role using `is_authorized()`.
2. **View Allocations**: Use `view_budget_allocations()` to retrieve current budget allocations.
3. **Filter Allocations**: Apply filters using `filter_budget_data()` to narrow down the allocations based on specific criteria.
4. **Update Usage**: Run `update_budget_usage()` to keep the budget allocations updated in real-time.
5. **Generate Alerts**: Set a threshold and use `generate_alerts()` to monitor and alert when budgets are exceeded.

## Example
```python
if __name__ == "__main__":
    if not is_authorized('finance_team'):
        print("Access denied. You are not authorized to view budget allocations.")
    else:
        update_thread = threading.Thread(target=update_budget_usage)
        update_thread.daemon = True
        update_thread.start()

        while True:
            time.sleep(1)
```

## Training Sessions
Training sessions will be conducted to familiarize finance team members with the system. The sessions will cover:
- System Overview
- Module Functions
- Practical Usage Scenarios
- Hands-on Exercises

Please contact the IT department to schedule a training session.