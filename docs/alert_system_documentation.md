# Alert System Configuration and Management

## Overview
The `alert_system.py` module is responsible for managing alerts within the Budget Allocation System. It provides functionalities to send alerts through various methods and define alert conditions based on user roles.

## Functions

### `send_alert(message, method='in_app', contact_info=None)`
- **Description**: Sends an alert using the specified method.
- **Parameters**:
  - `message` (str): The alert message to be sent.
  - `method` (str): The method of alert ('email', 'sms', 'in_app').
  - `contact_info` (str, optional): The contact information required for the alert method.

### `define_alert_conditions(role, conditions)`
- **Description**: Defines alert conditions for budget allocations.
- **Parameters**:
  - `role` (str): The role of the user defining the conditions.
  - `conditions` (dict): A dictionary of conditions to be set.
- **Raises**: `PermissionError` if the user is not authorized to define alert conditions.

## Usage
1. **Sending Alerts**: Use `send_alert()` to send alerts via email, SMS, or in-app notifications.
2. **Defining Alert Conditions**: Use `define_alert_conditions()` to set conditions for triggering alerts based on user roles.

## Training Sessions
Training sessions will be conducted to familiarize users with the alert system. The sessions will cover:
- Understanding Alert Methods
- Defining Alert Conditions
- Practical Usage Scenarios
- Hands-on Exercises

### Session Agenda
1. **Introduction to Alert System**
   - Overview of alert functionalities and importance.

2. **Detailed Walkthrough of Functions**
   - `send_alert()`: Sending alerts through different methods.
   - `define_alert_conditions()`: Setting up alert conditions.

3. **Hands-on Exercises**
   - Sending alerts using different methods.
   - Defining and testing alert conditions.

4. **Q&A Session**
   - Open floor for questions and clarifications.

## Feedback
Please provide feedback on the training session to help us improve future sessions.