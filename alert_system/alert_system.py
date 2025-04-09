import logging

# Setup logging
logging.basicConfig(filename='alerts.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def send_alert(message, method='in_app', contact_info=None):
    """
    Send an alert using the specified method.

    :param message: The alert message to be sent.
    :param method: The method of alert ('email', 'sms', 'in_app').
    :param contact_info: The contact information required for the alert method.
    """
    if method == 'email':
        send_email_alert(message, contact_info)
    elif method == 'sms':
        send_sms_alert(message, contact_info)
    else:
        send_in_app_alert(message)

    logging.info(f"Alert sent via {method}: {message}")


def send_email_alert(message, email):
    # Mock email sending
    print(f"Email sent to {email}: {message}")


def send_sms_alert(message, phone_number):
    # Mock SMS sending
    print(f"SMS sent to {phone_number}: {message}")


def send_in_app_alert(message):
    # Mock in-app notification
    print(f"In-app notification: {message}")


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