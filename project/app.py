from flask import Flask
from services.user_service import UserService
from services.role_service import RoleService
from services.permission_service import PermissionService
from middleware.access_control import AccessControlMiddleware
from audit.file_audit_trail import FileAuditTrail

app = Flask(__name__)

# Initialize audit trail
audit_trail = FileAuditTrail('audit_log.txt')

# Initialize services with audit trail
user_service = UserService(audit_trail)
role_service = RoleService(audit_trail)
permission_service = PermissionService(audit_trail)

# Initialize middleware
AccessControlMiddleware(app, user_service)

@app.route('/')
def home():
    return "Welcome to the Access Controlled Application!"

if __name__ == '__main__':
    app.run(debug=True)
