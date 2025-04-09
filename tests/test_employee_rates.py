import unittest
from employee_rates import get_hourly_rate

class TestEmployeeRates(unittest.TestCase):

    def test_authorized_access(self):
        # Test with an authorized role
        try:
            rate = get_hourly_rate(1, 'finance_team')
            self.assertEqual(rate, 50.0)
        except PermissionError:
            self.fail("get_hourly_rate() raised PermissionError unexpectedly!")

    def test_unauthorized_access(self):
        # Test with an unauthorized role
        with self.assertRaises(PermissionError):
            get_hourly_rate(1, 'guest')

if __name__ == '__main__':
    unittest.main()