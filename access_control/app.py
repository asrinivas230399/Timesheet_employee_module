from flask import Flask
from services.user_service import UserService
from middleware.access_control import AccessControlMiddleware

app = Flask(__name__)

# Initialize services
user_service = UserService()

# Initialize middleware
AccessControlMiddleware(app, user_service)

@app.route('/')
def home():
    return "Welcome to the Access Controlled Application!"

if __name__ == '__main__':
    app.run(debug=True)