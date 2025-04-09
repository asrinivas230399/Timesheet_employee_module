import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='access.log',
                    filemode='a')

class AuditTrail:
    @staticmethod
    def log_access(role: str, action: str):
        """
        Log access actions performed by a role.
        :param role: The role performing the action.
        :param action: The action being performed.
        """
        logging.info(f"Role '{role}' performed action '{action}'.")

    @staticmethod
    def log_modification(role: str, modification: str):
        """
        Log modifications made by a role.
        :param role: The role making the modification.
        :param modification: The modification being made.
        """
        logging.info(f"Role '{role}' made modification '{modification}'.")