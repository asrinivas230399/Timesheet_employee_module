from models.role import Role

class User:
    def __init__(self, username: str):
        self.username = username
        self.roles = set()

    def add_role(self, role: Role):
        self.roles.add(role)

    def remove_role(self, role: Role):
        self.roles.discard(role)

    def has_role(self, role: Role) -> bool:
        return role in self.roles

    def has_permission(self, permission) -> bool:
        return any(role.has_permission(permission) for role in self.roles)