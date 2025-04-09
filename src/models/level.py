class Level:
    def __init__(self, level_id: int, name: str, salary_range: tuple):
        self.level_id = level_id
        self.name = name
        self.salary_range = salary_range

    def get_salary_range(self) -> tuple:
        return self.salary_range

    def set_salary_range(self, new_salary_range: tuple):
        if not isinstance(new_salary_range, tuple) or len(new_salary_range) != 2:
            raise ValueError("Salary range must be a tuple with two elements.")
        self.salary_range = new_salary_range
