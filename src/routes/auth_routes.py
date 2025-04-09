from flask import Blueprint, request, jsonify
from src.services.auth_service import AuthService

# Create a Blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get('user_id')
    password = data.get('password')
    if auth_service.authenticate_user(user_id, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/check_permission', methods=['GET'])
def check_permission():
    user_id = request.args.get('user_id')
    required_role = request.args.get('required_role')
    if auth_service.is_authorized(user_id, required_role):
        return jsonify({'message': 'User is authorized'}), 200
    else:
        return jsonify({'message': 'User is not authorized'}), 403
