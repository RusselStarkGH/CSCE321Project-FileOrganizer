# Logging file for the app
from pathlib import Path
import logging

# This function sets up the logger for the app, which will log messages in the case of an error or crash. 
def setup_logger():
    log_path = Path(__file__).resolve().parent / "organizer.log"    # Create organizer.log only in this directory to avoid duplicates
    logging.basicConfig(
        filename=str(log_path),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
        )
    return logging.getLogger()

# Starts the logger
logger = setup_logger()
        