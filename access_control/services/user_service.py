from models.user import User
from models.role import Role

class UserService:
    def __init__(self):
        self.users = {}

    def add_user(self, username: str):
        if username not in self.users:
            self.users[username] = User(username)

    def remove_user(self, username: str):
        if username in self.users:
            del self.users[username]

    def get_user(self, username: str) -> User:
        return self.users.get(username)

    def assign_role_to_user(self, username: str, role: Role):
        user = self.get_user(username)
        if user:
            user.add_role(role)

    def remove_role_from_user(self, username: str, role: Role):
        user = self.get_user(username)
        if user:
            user.remove_role(role)