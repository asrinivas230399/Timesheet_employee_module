class Role:
    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name

    def __str__(self):
        return f"Role ID: {self.role_id}, Role Name: {self.role_name}"