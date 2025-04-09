# main.py
from employee_data import fetch_employee_data

def display_employee_dashboard():
    employees = fetch_employee_data()
    print("Employee Dashboard")
    print("-----------------")
    for employee in employees:
        print(f"ID: {employee['id']}, Name: {employee['name']}, Position: {employee['position']}")

if __name__ == "__main__":
    display_employee_dashboard()