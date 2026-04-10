# Logging file for the app

import logging

# This function sets up the logger for the app, which will log messages in the case of an error or crash. 
def setup_logger():
    logging.basicConfig(
        filename='organizer.log',
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
        )
    return logging.getLogger()

# Starts the logger
logger = setup_logger()
        