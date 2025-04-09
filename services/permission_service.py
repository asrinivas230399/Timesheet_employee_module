from models.permission import Permission

class PermissionService:
    def __init__(self):
        self.permissions = {}

    def add_permission(self, permission_name: str):
        if permission_name not in self.permissions:
            self.permissions[permission_name] = Permission(permission_name)
            print(f"Permission '{permission_name}' added.")

    def remove_permission(self, permission_name: str):
        if permission_name in self.permissions:
            del self.permissions[permission_name]
            print(f"Permission '{permission_name}' removed.")

    def get_permission(self, permission_name: str) -> Permission:
        return self.permissions.get(permission_name)

    def list_permissions(self):
        return list(self.permissions.keys())