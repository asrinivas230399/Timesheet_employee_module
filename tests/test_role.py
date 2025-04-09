import unittest
from models.role import Role

class TestRole(unittest.TestCase):
    def test_add_permission(self):
        role = Role("admin")
        role.add_permission("read")
        self.assertTrue(role.has_permission("read"))

    def test_remove_permission(self):
        role = Role("admin")
        role.add_permission("write")
        role.remove_permission("write")
        self.assertFalse(role.has_permission("write"))

if __name__ == '__main__':
    unittest.main()
