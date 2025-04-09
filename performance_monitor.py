import time
from contextlib import contextmanager

@contextmanager
def performance_monitor(action_name: str):
    """
    Context manager to monitor the performance of a block of code.
    :param action_name: The name of the action being monitored.
    """
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(f"{action_name} took {duration:.4f} seconds.")