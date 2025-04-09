from audit.audit_trail import AuditTrail
from audit.key_management_service import KeyManagementService
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class FileAuditTrail(AuditTrail):
    def __init__(self, file_path: str, key_service: KeyManagementService):
        self.file_path = file_path
        self.key_service = key_service

    def log_action(self, action: str, entity: str, name: str):
        log_entry = f"Action: {action}, Entity: {entity}, Name: {name}"
        signature = self.key_service.private_key.sign(
            log_entry.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        with open(self.file_path, 'a') as file:
            file.write(f"{log_entry}\nSignature: {signature.hex()}\n")

    def verify_log(self, log_entry: str, signature: str) -> bool:
        try:
            self.key_service.public_key.verify(
                bytes.fromhex(signature),
                log_entry.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False