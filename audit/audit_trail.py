class AuditTrail:
    def log_action(self, action: str, entity: str, name: str):
        raise NotImplementedError("Subclasses should implement this method.")