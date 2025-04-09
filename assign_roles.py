# Import dependencies
from auth import authenticate_user, check_permission
from logging import log_action, log_error
from database import get_user, update_user_roles

roles = {
    'admin': ['assign_roles', 'view_reports', 'manage_users'],
    'editor': ['edit_content', 'view_reports'],
    'viewer': ['view_reports']
}

def is_authorized(user, action):
    """
    Check if the user has the authorization to perform a specific action.
    """
    return check_permission(user, action)

def assign_role_to_user(current_user, target_user, role):
    """
    Assign a role to a target user if the current user is authorized to do so.
    """
    if not is_authorized(current_user, 'assign_roles'):
        log_error(f"Unauthorized access attempt by {current_user['username']}")
        return "Unauthorized: You do not have permission to assign roles."

    if role not in roles:
        log_error(f"Attempt to assign non-existent role '{role}' by {current_user['username']}")
        return f"Error: The role '{role}' does not exist."

    target_user_details = get_user(target_user['username'])
    if role in target_user_details.get('roles', []):
        return f"User already has the role '{role}'."

    target_user_details['roles'].append(role)
    update_user_roles(target_user['username'], target_user_details['roles'])
    log_action(f"Role '{role}' assigned to {target_user['username']} by {current_user['username']}")
    return f"Role '{role}' has been successfully assigned to the user."

# Example usage
if __name__ == "__main__":
    admin_user = {'username': 'admin', 'roles': ['admin']}
    normal_user = {'username': 'john_doe', 'roles': []}

    print(assign_role_to_user(admin_user, normal_user, 'editor'))
    print(assign_role_to_user(normal_user, normal_user, 'viewer'))