from models.permission import Permission
from audit.audit_trail import AuditTrail

class PermissionService:
    def __init__(self, audit_trail: AuditTrail):
        self.permissions = {}

    def add_permission(self, permission_name: str):
        if permission_name not in self.permissions:
            self.permissions[permission_name] = Permission(permission_name)
            self.audit_trail.log_action("add", "permission", permission_name)

    def remove_permission(self, permission_name: str):
        if permission_name in self.permissions:
            del self.permissions[permission_name]
            self.audit_trail.log_action("remove", "permission", permission_name)

    def get_permission(self, permission_name: str) -> Permission:
        return self.permissions.get(permission_name)

    def list_permissions(self):
        return list(self.permissions.keys())
