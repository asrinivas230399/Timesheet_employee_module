import unittest
from services.role_service import RoleService

class TestRoleService(unittest.TestCase):
    def test_add_role(self):
        service = RoleService()
        service.add_role("admin")
        self.assertIsNotNone(service.get_role("admin"))

    def test_remove_role(self):
        service = RoleService()
        service.add_role("admin")
        service.remove_role("admin")
        self.assertIsNone(service.get_role("admin"))

if __name__ == '__main__':
    unittest.main()
