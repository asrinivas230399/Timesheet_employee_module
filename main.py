from services.user_service import get_all_users, delete_user, log_activity, generate_dashboard, export_cost_data

def main():
    # Example usage
    try:
        requesting_user_id = int(input("Enter your user ID: "))

        print("All users:")
        for user in get_all_users(requesting_user_id):
            print(user)

        # Delete a user
        user_id_to_delete = int(input("Enter the user ID to delete: "))
        delete_user(requesting_user_id, user_id_to_delete)

        # Log an admin action
        log_activity("Deleted a user", requesting_user_id)

        # Generate dashboard
        generate_dashboard(requesting_user_id)

        # Export cost data
        export_format = input("Enter export format (csv/json): ")
        export_cost_data(export_format)

    except PermissionError as e:
        print(f"Permission Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
