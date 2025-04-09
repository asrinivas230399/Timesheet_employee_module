# role_assigner.py

from auth import check_permission
from logging import log_action, log_error
from database import get_user, update_user_roles
from event_system import event_system

roles = {
    'admin': ['assign_roles', 'view_reports', 'manage_users'],
    'editor': ['edit_content', 'view_reports'],
    'viewer': ['view_reports']
}

class RoleAssigner:
    def __init__(self, current_user):
        self.current_user = current_user

    def is_authorized(self, action):
        """
        Check if the current user has the authorization to perform a specific action.
        """
        return check_permission(self.current_user, action)

    def assign_role(self, target_user, role):
        """
        Assign a role to a target user if the current user is authorized to do so.
        """
        if not self.is_authorized('assign_roles'):
            log_error(f"Unauthorized access attempt by {self.current_user['username']}")
            return "Unauthorized: You do not have permission to assign roles."

        if role not in roles:
            log_error(f"Attempt to assign non-existent role '{role}' by {self.current_user['username']}")
            return f"Error: The role '{role}' does not exist."

        target_user_details = get_user(target_user['username'])
        if role in target_user_details.get('roles', []):
            return f"User already has the role '{role}'."

        target_user_details['roles'].append(role)
        update_user_roles(target_user['username'], target_user_details['roles'])
        log_action(f"Role '{role}' assigned to {target_user['username']} by {self.current_user['username']}")

        # Publish the role assignment event
        event_system.publish('role_assigned', {
            'assigned_by': self.current_user['username'],
            'target_user': target_user['username'],
            'role': role
        })

        return f"Role '{role}' has been successfully assigned to the user."

# Example usage
if __name__ == "__main__":
    def on_role_assigned(data):
        print(f"Real-time update: {data['role']} role assigned to {data['target_user']} by {data['assigned_by']}")

    event_system.subscribe('role_assigned', on_role_assigned)

    admin_user = {'username': 'admin', 'roles': ['admin']}
    normal_user = {'username': 'john_doe', 'roles': []}

    role_assigner = RoleAssigner(admin_user)
    print(role_assigner.assign_role(normal_user, 'editor'))

    role_assigner = RoleAssigner(normal_user)
    print(role_assigner.assign_role(normal_user, 'viewer'))
