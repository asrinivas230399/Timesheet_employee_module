import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class KeyManagementService:
    def __init__(self, private_key_file: str, public_key_file: str):
        self.private_key_file = private_key_file
        self.public_key_file = public_key_file
        self.private_key, self.public_key = self.load_keys()

    def generate_keys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()

        with open(self.private_key_file, 'wb') as private_file:
            private_file.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        with open(self.public_key_file, 'wb') as public_file:
            public_file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        return private_key, public_key

    def load_keys(self):
        if not os.path.exists(self.private_key_file) or not os.path.exists(self.public_key_file):
            return self.generate_keys()

        with open(self.private_key_file, 'rb') as private_file:
            private_key = serialization.load_pem_private_key(
                private_file.read(),
                password=None
            )

        with open(self.public_key_file, 'rb') as public_file:
            public_key = serialization.load_pem_public_key(
                public_file.read()
            )

        return private_key, public_key