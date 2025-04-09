import logging

# Setup logging
logging.basicConfig(filename='access.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def is_authorized(role):
    # Mock authorization check
    authorized_roles = ['finance_team', 'admin']
    return role in authorized_roles

def define_roles():
    # Define roles and their permissions
    roles_permissions = {
        'finance_team': ['view_budget', 'edit_budget'],
        'admin': ['view_budget', 'edit_budget', 'manage_users'],
        'guest': ['view_budget'],
    }
    return roles_permissions

def check_access(role, permission):
    roles_permissions = define_roles()
    if role in roles_permissions:
        access_granted = permission in roles_permissions[role]
        # Log the access attempt
        logging.info(f"Role '{role}' attempted to access '{permission}': {'Granted' if access_granted else 'Denied'}")
        return access_granted
    # Log the access attempt
    logging.info(f"Role '{role}' attempted to access '{permission}': Denied")
    return False

def audit_access_log():
    # Function to audit access logs
    with open('access.log', 'r') as log_file:
        logs = log_file.readlines()
        # Process logs for auditing
        for log in logs:
            print(log.strip())

# Example usage of audit
if __name__ == "__main__":
    audit_access_log()