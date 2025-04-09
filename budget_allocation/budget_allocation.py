from .employee_rates import get_hourly_rate
from .role_based_access import is_authorized
import threading
import time
from alert_system.alert_system import send_alert
from cryptography.fernet import Fernet
import logging

# Setup logging
logging.basicConfig(filename='access.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def view_budget_allocations():
    # Mock data for employee allocations
    employee_allocations = [
        {'employee_id': 1, 'allocated_hours': 160, 'project': 'Project A', 'date': '2023-10-01'},
        {'employee_id': 2, 'allocated_hours': 120, 'project': 'Project B', 'date': '2023-10-02'},
        {'employee_id': 3, 'allocated_hours': 140, 'project': 'Project A', 'date': '2023-10-03'},
    ]

    budget_allocations = []

    for allocation in employee_allocations:
        employee_id = allocation['employee_id']
        allocated_hours = allocation['allocated_hours']
        hourly_rate = get_hourly_rate(employee_id)
        total_cost = allocated_hours * hourly_rate
        encrypted_total_cost = cipher_suite.encrypt(str(total_cost).encode())
        budget_allocations.append({
            'employee_id': employee_id,
            'allocated_hours': allocated_hours,
            'hourly_rate': hourly_rate,
            'total_cost': encrypted_total_cost,
            'project': allocation['project'],
            'date': allocation['date']
        })

    return budget_allocations


def filter_budget_data(employee_id=None, project=None, start_date=None, end_date=None):
    allocations = view_budget_allocations()
    filtered_allocations = []

    for allocation in allocations:
        if employee_id is not None and allocation['employee_id'] != employee_id:
            continue
        if project is not None and allocation['project'] != project:
            continue
        if start_date is not None and allocation['date'] < start_date:
            continue
        if end_date is not None and allocation['date'] > end_date:
            continue
        filtered_allocations.append(allocation)

    return filtered_allocations


def update_budget_usage():
    while True:
        allocations = view_budget_allocations()
        print("Updated Budget Allocations:")
        for allocation in allocations:
            decrypted_total_cost = cipher_suite.decrypt(allocation['total_cost']).decode()
            print({**allocation, 'total_cost': decrypted_total_cost})
        time.sleep(60)  # Refresh every 60 seconds


def generate_alerts(threshold):
    allocations = view_budget_allocations()
    for allocation in allocations:
        decrypted_total_cost = float(cipher_suite.decrypt(allocation['total_cost']).decode())
        if decrypted_total_cost > threshold:
            send_alert(f"Budget exceeded for employee {allocation['employee_id']} on project {allocation['project']}.")


# Example usage
if __name__ == "__main__":
    # Check if the user is authorized
    if not is_authorized('finance_team'):
        print("Access denied. You are not authorized to view budget allocations.")
    else:
        logging.info("User authorized to view budget allocations.")
        # Start the background task to update budget usage
        update_thread = threading.Thread(target=update_budget_usage)
        update_thread.daemon = True
        update_thread.start()

        # Keep the main thread alive
        while True:
            time.sleep(1)
