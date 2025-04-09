class Role:
    def __init__(self, name: str):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)
        print(f"Permission '{permission}' added to role '{self.name}'.")

    def remove_permission(self, permission):
        self.permissions.discard(permission)
        print(f"Permission '{permission}' removed from role '{self.name}'.")

    def has_permission(self, permission) -> bool:
        return permission in self.permissions