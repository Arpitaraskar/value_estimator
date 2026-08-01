# from pathlib import Path
# import logging
# from logging.handlers import RotatingFileHandler

# file_handler = logging.FileHandler(LOG_FILE)

# BASE_DIR = Path(__file__).resolve().parent.parent.parent

# LOGS_DIR = BASE_DIR / "logs"

# LOGS_DIR.mkdir(exist_ok=True)

# LOG_FILE = LOGS_DIR / "app.log"



# logging.basicConfig(
#     level=logging.INFO,
#       format="%(asctime)s | %(levelname)s | %(message)s",
#       handlers=[
#           logging.StreamHandler(), #terminal logs
#           logging.FileHandler(LOG_FILE) # files logs see in logs/app.log folder
#       ]
# )

# logger = logging.getLogger(__name__)

# to add rotatefilehandler 

from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

BASE_DIR = Path(__file__).resolve().parent.parent.parent

LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

LOG_FILE = LOGS_DIR / "app.log"

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=500,      # 500 bytes (for testing only)
    backupCount=5
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        file_handler
    ]
)

logger = logging.getLogger(__name__)