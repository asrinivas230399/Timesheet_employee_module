import unittest
from models.permission import Permission

class TestPermission(unittest.TestCase):
    def test_permission_creation(self):
        permission = Permission("read")
        self.assertEqual(permission.name, "read")

if __name__ == '__main__':
    unittest.main()
