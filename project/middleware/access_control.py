from flask import request, abort
from services.user_service import UserService

class AccessControlMiddleware:
    def __init__(self, app, user_service: UserService):
        self.app = app
        self.user_service = user_service
        self.app.before_request(self.check_permissions)

    def check_permissions(self):
        username = request.headers.get('X-User')
        required_permission = request.headers.get('X-Permission')

        if not username or not required_permission:
            self.log_unauthorized_access(username, required_permission)
            abort(403)

        user = self.user_service.get_user(username)
        if not user or not user.has_permission(required_permission):
            self.log_unauthorized_access(username, required_permission)
            abort(403)

    def log_unauthorized_access(self, username, permission):
        print(f"Unauthorized access attempt by user '{username}' for permission '{permission}'.")
