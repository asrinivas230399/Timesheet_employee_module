import unittest
from services.permission_service import PermissionService

class TestPermissionService(unittest.TestCase):
    def test_add_permission(self):
        service = PermissionService()
        service.add_permission("read")
        self.assertIsNotNone(service.get_permission("read"))

    def test_remove_permission(self):
        service = PermissionService()
        service.add_permission("write")
        service.remove_permission("write")
        self.assertIsNone(service.get_permission("write"))

if __name__ == '__main__':
    unittest.main()
