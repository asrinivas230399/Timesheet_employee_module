# test_performance.py

import time
from budget_allocation.budget_allocation import view_budget_allocations

def test_performance():
    start_time = time.time()
    allocations = view_budget_allocations()
    end_time = time.time()
    print(f"Retrieved {len(allocations)} allocations in {end_time - start_time:.4f} seconds.")

if __name__ == "__main__":
    test_performance()
