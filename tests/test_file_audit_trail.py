import unittest
from audit.file_audit_trail import FileAuditTrail

class TestFileAuditTrail(unittest.TestCase):
    def setUp(self):
        self.audit_trail = FileAuditTrail('test_audit_log.txt')

    def test_log_action(self):
        self.audit_trail.log_action("add", "role", "admin")
        with open('test_audit_log.txt', 'r') as file:
            logs = file.readlines()
        self.assertIn("Action: add, Entity: role, Name: admin\n", logs)

    def tearDown(self):
        import os
        os.remove('test_audit_log.txt')

if __name__ == '__main__':
    unittest.main()
