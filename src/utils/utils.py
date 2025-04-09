import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Encryption key (should be stored securely)
ENCRYPTION_KEY = Fernet.generate_key()
fernet = Fernet(ENCRYPTION_KEY)

def encrypt_data(data: str) -> str:
    """
    Encrypts the given data using Fernet symmetric encryption.

    :param data: The data to encrypt
    :return: The encrypted data as a string
    """
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str) -> str:
    """
    Decrypts the given encrypted data using Fernet symmetric encryption.

    :param encrypted_data: The encrypted data to decrypt
    :return: The decrypted data as a string
    """
    return fernet.decrypt(encrypted_data.encode()).decode()

def log_info(message: str):
    """
    Logs an info level message.

    :param message: The message to log
    """
    logger.info(message)

def log_error(message: str):
    """
    Logs an error level message.

    :param message: The message to log
    """
    logger.error(message)