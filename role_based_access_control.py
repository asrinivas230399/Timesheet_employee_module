class RoleBasedAccessControl:
    def __init__(self):
        # Define roles and their permissions
        self.roles_permissions = {
            'admin': ['encrypt', 'decrypt', 'manage_users'],
            'user': ['encrypt', 'decrypt'],
            'guest': []
        }
        
    def has_permission(self, role: str, permission: str) -> bool:
        """
        Check if a role has a specific permission.
        :param role: The role to check.
        :param permission: The permission to check for.
        :return: True if the role has the permission, False otherwise.
        """
        return permission in self.roles_permissions.get(role, [])

    def add_role(self, role: str, permissions: list):
        """
        Add a new role with specific permissions.
        :param role: The role to add.
        :param permissions: A list of permissions for the role.
        """
        self.roles_permissions[role] = permissions

    def remove_role(self, role: str):
        """
        Remove a role from the system.
        :param role: The role to remove.
        """
        if role in self.roles_permissions:
            del self.roles_permissions[role]

    def update_permissions(self, role: str, permissions: list):
        """
        Update permissions for an existing role.
        :param role: The role to update.
        :param permissions: A new list of permissions for the role.
        """
        if role in self.roles_permissions:
            self.roles_permissions[role] = permissions