# budget_allocation.py

from employee_rates import get_hourly_rate

def view_budget_allocations():
    # Mock data for employee allocations
    employee_allocations = [
        {'employee_id': 1, 'allocated_hours': 160},
        {'employee_id': 2, 'allocated_hours': 120},
        {'employee_id': 3, 'allocated_hours': 140},
    ]

    budget_allocations = []

    for allocation in employee_allocations:
        employee_id = allocation['employee_id']
        allocated_hours = allocation['allocated_hours']
        hourly_rate = get_hourly_rate(employee_id)
        total_cost = allocated_hours * hourly_rate
        budget_allocations.append({
            'employee_id': employee_id,
            'allocated_hours': allocated_hours,
            'hourly_rate': hourly_rate,
            'total_cost': total_cost
        })

    return budget_allocations

# Example usage
if __name__ == "__main__":
    allocations = view_budget_allocations()
    for allocation in allocations:
        print(allocation)
