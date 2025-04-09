from models.role import Role

class RoleService:
    def __init__(self):
        self.roles = {}

    def add_role(self, role_name: str):
        if role_name not in self.roles:
            self.roles[role_name] = Role(role_name)
            print(f"Role '{role_name}' added.")

    def remove_role(self, role_name: str):
        if role_name in self.roles:
            del self.roles[role_name]
            print(f"Role '{role_name}' removed.")

    def get_role(self, role_name: str) -> Role:
        return self.roles.get(role_name)

    def list_roles(self):
        return list(self.roles.keys())