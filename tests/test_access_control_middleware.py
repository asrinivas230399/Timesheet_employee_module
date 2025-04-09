import unittest
from flask import Flask
from services.user_service import UserService
from middleware.access_control import AccessControlMiddleware
from models.role import Role

class TestAccessControlMiddleware(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.user_service = UserService()
        self.middleware = AccessControlMiddleware(self.app, self.user_service)
        self.client = self.app.test_client()

    def test_access_control(self):
        self.user_service.add_user("john")
        role = Role("admin")
        role.add_permission("access_home")
        self.user_service.assign_role_to_user("john", role)

        @self.app.route('/home')
        def home():
            return "Home Page"

        with self.app.test_request_context('/home', headers={"X-User": "john", "X-Permission": "access_home"}):
            response = self.client.get('/home')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
