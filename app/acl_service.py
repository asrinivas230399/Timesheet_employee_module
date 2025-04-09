import logging
import httpx  # For asynchronous HTTP requests

class ACLService:
    def __init__(self, acl_api_url: str):
        self.acl_api_url = acl_api_url

    async def fetch_roles(self):
        """
        Fetches role-based access information from the ACL system.
        """
        logging.info("Fetching roles from ACL system.")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.acl_api_url}/roles")
                response.raise_for_status()
                roles = response.json()
                logging.info("Roles fetched successfully from ACL system.")
                return roles
        except httpx.RequestError as e:
            logging.error(f"Error fetching roles from ACL system: {e}")
            return None

    async def update_roles(self, roles):
        """
        Updates role-based access information in the ACL system.
        """
        logging.info("Updating roles in ACL system.")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(f"{self.acl_api_url}/roles/update", json=roles)
                response.raise_for_status()
                logging.info("Roles updated successfully in ACL system.")
                return response.status_code
        except httpx.RequestError as e:
            logging.error(f"Error updating roles in ACL system: {e}")
            return None

    async def is_user_authorized(self, user_id: str, action: str) -> bool:
        """
        Checks if a user is authorized to perform a specific action based on ACL.
        """
        logging.info(f"Checking authorization for user {user_id} to perform {action}.")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.acl_api_url}/authorize", params={"user_id": user_id, "action": action})
                response.raise_for_status()
                is_authorized = response.json().get("authorized", False)
                logging.info(f"Authorization check for user {user_id} returned: {is_authorized}.")
                return is_authorized
        except httpx.RequestError as e:
            logging.error(f"Error checking authorization for user {user_id}: {e}")
            return False
