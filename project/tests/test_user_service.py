import unittest
from services.user_service import UserService
from models.role import Role

class TestUserService(unittest.TestCase):
    def test_add_user(self):
        service = UserService()
        service.add_user("john")
        self.assertIsNotNone(service.get_user("john"))

    def test_remove_user(self):
        service = UserService()
        service.add_user("john")
        service.remove_user("john")
        self.assertIsNone(service.get_user("john"))

    def test_assign_role_to_user(self):
        service = UserService()
        service.add_user("john")
        role = Role("admin")
        service.assign_role_to_user("john", role)
        user = service.get_user("john")
        self.assertTrue(user.has_role(role))

if __name__ == '__main__':
    unittest.main()
