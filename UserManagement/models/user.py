class User:
    def __init__(self, user_id, name, role, access_level):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.access_level = access_level

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name}, role={self.role}, access_level={self.access_level})"