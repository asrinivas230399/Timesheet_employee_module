import logging

# Function to set up logging configuration
# Logs are stored in a file and can be retrieved for audit purposes

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Logs are stored in a file named app.log
            logging.StreamHandler()  # Logs are also output to the console
        ]
    )