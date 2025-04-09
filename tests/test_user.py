import unittest
from models.user import User
from models.role import Role

class TestUser(unittest.TestCase):
    def test_add_role(self):
        user = User("john")
        role = Role("admin")
        user.add_role(role)
        self.assertTrue(user.has_role(role))

    def test_remove_role(self):
        user = User("john")
        role = Role("admin")
        user.add_role(role)
        user.remove_role(role)
        self.assertFalse(user.has_role(role))

if __name__ == '__main__':
    unittest.main()
