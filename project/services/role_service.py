from models.role import Role
from audit.audit_trail import AuditTrail

class RoleService:
    def __init__(self, audit_trail: AuditTrail):
        self.roles = {}
        self.audit_trail = audit_trail

    def add_role(self, role_name: str):
        if role_name not in self.roles:
            self.roles[role_name] = Role(role_name)
            self.audit_trail.log_action("add", "role", role_name)

    def remove_role(self, role_name: str):
        if role_name in self.roles:
            del self.roles[role_name]
            self.audit_trail.log_action("remove", "role", role_name)

    def get_role(self, role_name: str) -> Role:
        return self.roles.get(role_name)

    def list_roles(self):
        return list(self.roles.keys())
