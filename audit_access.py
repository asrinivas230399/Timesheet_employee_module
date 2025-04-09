import logging

# Setup logging
logging.basicConfig(filename='access.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def audit_access_log():
    # Function to audit access logs
    with open('access.log', 'r') as log_file:
        logs = log_file.readlines()
        # Process logs for auditing
        for log in logs:
            print(log.strip())

# Example usage of audit
if __name__ == "__main__":
    audit_access_log()