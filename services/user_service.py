import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.user import User, Base
from data.cost_data import cost_data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
engine = create_engine('sqlite:///users.db')
Session = sessionmaker(bind=engine)
session = Session()


def get_all_users(requesting_user_id):
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


def delete_user(requesting_user_id, user_id_to_delete):
    requesting_user = session.query(User).filter_by(user_id=requesting_user_id).first()
    if not requesting_user:
        logging.warning("User ID not found.")
        raise ValueError("User ID not found.")
    
    if requesting_user.role == "Admin":
        user_to_delete = session.query(User).filter_by(user_id=user_id_to_delete).first()
        if user_to_delete:
            confirmation = input(f"Are you sure you want to delete {user_to_delete.name}? (yes/no): ")
            if confirmation.lower() == 'yes':
                session.delete(user_to_delete)
                session.commit()
                logging.info(f"User {user_to_delete.name} has been deleted.")
                print(f"User {user_to_delete.name} has been deleted.")
            else:
                logging.info(f"Deletion of user {user_to_delete.name} cancelled.")
                print("Deletion cancelled.")
        else:
            logging.warning(f"User with ID {user_id_to_delete} not found.")
            print("User not found.")
    else:
        logging.warning("Unauthorized access attempt to delete a user.")
        raise PermissionError("You do not have permission to delete users.")


def log_activity(action, user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    if not user:
        logging.warning("User ID not found.")
        raise ValueError("User ID not found.")
    
    if user.role == "Admin":
        logging.info(f"Admin action: {action} performed by User ID: {user_id}")
    else:
        logging.warning("Unauthorized access attempt to log an activity.")
        raise PermissionError("You do not have permission to log activities.")


def get_cost_data(requesting_user_id):
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


def generate_dashboard(requesting_user_id):
    requesting_user = session.query(User).filter_by(user_id=requesting_user_id).first()
    if not requesting_user:
        logging.warning("User ID not found.")
        raise ValueError("User ID not found.")
    
    if requesting_user.role in ["Admin", "Finance"]:
        logging.info("Generating dashboard.")
        cost_data = get_cost_data(requesting_user_id)
        print("\n--- Cost Dashboard ---")
        for user_id, data in cost_data.items():
            print(f"User ID: {user_id}, Hourly Rate: {data['hourly_rate']}, Employment Terms: {data['employment_terms']}")
        print("----------------------\n")
    else:
        logging.warning("Unauthorized access attempt to generate dashboard.")
        raise PermissionError("You do not have permission to generate the dashboard.")


def export_cost_data(format):
    if format == 'csv':
        with open('cost_data.csv', 'w') as file:
            file.write('user_id,hourly_rate,employment_terms\n')
            for user_id, data in cost_data.items():
                file.write(f"{user_id},{data['hourly_rate']},{data['employment_terms']}\n")
        logging.info("Cost data exported to cost_data.csv")
    elif format == 'json':
        import json
        with open('cost_data.json', 'w') as file:
            json.dump(cost_data, file)
        logging.info("Cost data exported to cost_data.json")
    else:
        logging.warning("Unsupported export format.")
        raise ValueError("Unsupported format. Please use 'csv' or 'json'.")
