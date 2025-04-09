from audit.audit_trail import AuditTrail

class FileAuditTrail(AuditTrail):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def log_action(self, action: str, entity: str, name: str):
        with open(self.file_path, 'a') as file:
            file.write(f"Action: {action}, Entity: {entity}, Name: {name}\n")
