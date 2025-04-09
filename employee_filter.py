from auth import check_permission

class EmployeeFilter:
    def __init__(self, employees, current_user):
        """
        Initialize the EmployeeFilter with a list of employees and the current user.
        :param employees: List of employee dictionaries.
        :param current_user: The user performing the filtering.
        """
        self.employees = employees
        self.current_user = current_user

    def is_authorized(self, action):
        """
        Check if the current user has the authorization to perform a specific action.
        """
        return check_permission(self.current_user, action)

    def apply_filters(self, filters):
        """
        Apply a series of filters to the employee list.
        :param filters: A dictionary of filters to apply.
        :return: List of employees that match all filters.
        """
        filtered_employees = self.employees

        if 'department' in filters:
            filtered_employees = [emp for emp in filtered_employees if emp.get('department') == filters['department']]

        if 'role' in filters:
            filtered_employees = [emp for emp in filtered_employees if filters['role'] in emp.get('roles', [])]

        if 'min_experience' in filters:
            filtered_employees = [emp for emp in filtered_employees if emp.get('experience', 0) >= filters['min_experience']]

        return filtered_employees

# Example usage
if __name__ == "__main__":
    employees = [
        {'name': 'Alice', 'department': 'Engineering', 'roles': ['developer'], 'experience': 5},
        {'name': 'Bob', 'department': 'HR', 'roles': ['recruiter'], 'experience': 3},
        {'name': 'Charlie', 'department': 'Engineering', 'roles': ['developer', 'team lead'], 'experience': 8},
    ]

    current_user = {'username': 'admin', 'roles': ['admin']}
    filter = EmployeeFilter(employees, current_user)

    if filter.is_authorized('view_reports'):
        filters = {'department': 'Engineering', 'role': 'developer', 'min_experience': 5}
        print("Filtered Employees:", filter.apply_filters(filters))
    else:
        print("Unauthorized: You do not have permission to view reports.")