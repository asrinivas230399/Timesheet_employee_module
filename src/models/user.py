class User:
    def __init__(self, user_id: int, name: str, level: int):
        self.user_id = user_id
        self.name = name
        self.level = level
        self.validate_level()

    def validate_level(self):
        if not isinstance(self.level, int) or self.level < 0:
            raise ValueError("Level must be a non-negative integer.")

    def set_level(self, new_level: int):
        if not isinstance(new_level, int) or new_level < 0:
            raise ValueError("Level must be a non-negative integer.")
        self.level = new_level

    def get_level(self) -> int:
        return self.level