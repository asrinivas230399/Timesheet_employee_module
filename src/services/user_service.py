from models.user import User

class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id: int, name: str, level: int):
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        user = User(user_id=user_id, name=name, level=level)
        self.users[user_id] = user
        return user

    def assign_level(self, user_id: int, new_level: int):
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        user = self.users[user_id]
        user.set_level(new_level)
        return user

    def validate_level_assignment(self, user_id: int, level: int):
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        user = self.users[user_id]
        if user.level != level:
            raise ValueError("Level assignment is not valid.")
        return True