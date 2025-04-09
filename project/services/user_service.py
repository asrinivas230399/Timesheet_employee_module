from models.user import User
from models.role import Role
from audit.audit_trail import AuditTrail

class UserService:
    def __init__(self, audit_trail: AuditTrail):
        self.users = {}
        self.audit_trail = audit_trail

    def add_user(self, username: str):
        if username not in self.users:
            self.users[username] = User(username)
            self.audit_trail.log_action("add", "user", username)

    def remove_user(self, username: str):
        if username in self.users:
            del self.users[username]
            self.audit_trail.log_action("remove", "user", username)

    def get_user(self, username: str) -> User:
        return self.users.get(username)

    def assign_role_to_user(self, username: str, role: Role):
        user = self.get_user(username)
        if user:
            user.add_role(role)
            self.audit_trail.log_action("assign_role", "user", f"{username} -> {role.name}")

    def remove_role_from_user(self, username: str, role: Role):
        user = self.get_user(username)
        if user:
            user.remove_role(role)
            self.audit_trail.log_action("remove_role", "user", f"{username} -> {role.name}")
