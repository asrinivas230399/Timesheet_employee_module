import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.user import User, Base
from data.cost_data import cost_data
from pmo.pmo_system import get_real_time_user_data, get_real_time_cost_data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
engine = create_engine('sqlite:///users.db')
Session = sessionmaker(bind=engine)
session = Session()


def update_user_data():
    # Fetch real-time user data from PMO system
    real_time_users = get_real_time_user_data()
    for user_data in real_time_users:
        user = session.query(User).filter_by(user_id=user_data['user_id']).first()
        if user:
            user.name = user_data['name']
            user.role = user_data['role']
            user.access_level = user_data['access_level']
        else:
            new_user = User(**user_data)
            session.add(new_user)
    session.commit()


def update_cost_data():
    # Fetch real-time cost data from PMO system
    real_time_costs = get_real_time_cost_data()
    cost_data.update(real_time_costs)


def get_all_users(requesting_user_id):
    update_user_data()  # Ensure data is up-to-date
    requesting_user = session.query(User).filter_by(user_id=requesting_user_id).first()
    if not requesting_user:
        logging.warning("User ID not found.")
        raise ValueError("User ID not found.")
    
    if requesting_user.role == "Admin":
        logging.info("Accessed all users.")
        return session.query(User).all()
    else:
        logging.warning("Unauthorized access attempt to get all users.")
        raise PermissionError("You do not have permission to access this resource.")


def get_cost_data(requesting_user_id):
    update_cost_data()  # Ensure data is up-to-date
    requesting_user = session.query(User).filter_by(user_id=requesting_user_id).first()
    if not requesting_user:
        logging.warning("User ID not found.")
        raise ValueError("User ID not found.")
    
    if requesting_user.role == "Finance":
        logging.info("Accessed cost data.")
        return cost_data
    else:
        logging.warning("Unauthorized access attempt to get cost data.")
        raise PermissionError("You do not have permission to access cost data.")