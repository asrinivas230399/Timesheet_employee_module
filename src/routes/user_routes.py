from flask import Flask, request, jsonify
from models.user import User

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user_id = data['user_id']
        name = data['name']
        level = data['level']
        
        # Create a new User instance
        user = User(user_id=user_id, name=name, level=level)
        
        return jsonify({
            'user_id': user.user_id,
            'name': user.name,
            'level': user.get_level()
        }), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)