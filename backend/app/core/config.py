from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# ML Model
MODEL_NAME = "house_model.joblib"
MODEL_PATH = BASE_DIR / "ml" / "house_model.joblib"

# Prediction Settings
PRICE_MULTIPLIER = 100000
AVERAGE_ERROR = 39000

# API Information
APP_NAME = "California House Prediction API"
APP_VERSION = "1.0.0"

# Database
DATABASE_NAME = "prediction.db"
DATABASE_PATH = BASE_DIR.parent / "data" / DATABASE_NAME

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"