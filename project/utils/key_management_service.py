import os
from cryptography.fernet import Fernet

class KeyManagementService:
    def __init__(self, key_file: str):
        self.key_file = key_file
        self.key = self.load_key()

    def generate_key(self) -> bytes:
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as file:
            file.write(key)
        return key

    def load_key(self) -> bytes:
        if not os.path.exists(self.key_file):
            return self.generate_key()
        with open(self.key_file, 'rb') as file:
            return file.read()
