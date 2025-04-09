import logging

# Setup logging
logging.basicConfig(filename='alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def send_alert(message):
    # Mock alert sending
    print(f"ALERT: {message}")
    logging.info(f"Alert sent: {message}")


def define_alert_conditions(role, conditions):
    """
    Define alert conditions for budget allocations.

    :param role: The role of the user defining the conditions.
    :param conditions: A dictionary of conditions to be set.
    :raises PermissionError: If the user is not authorized to define alert conditions.
    """
    # Check if the user is authorized to define alert conditions
    if not check_access(role, 'define_alert_conditions'):
        raise PermissionError("Access denied. You are not authorized to define alert conditions.")

    # Log the alert conditions definition
    logging.info(f"Alert conditions defined by {role}: {conditions}")

    # Mock implementation of setting alert conditions
    # In a real implementation, this would update a configuration file or database
    print(f"Alert conditions set: {conditions}")


# Example usage of defining alert conditions
if __name__ == "__main__":
    try:
        define_alert_conditions('admin', {'threshold': 1000, 'frequency': 'daily'})
    except PermissionError as e:
        print(e)