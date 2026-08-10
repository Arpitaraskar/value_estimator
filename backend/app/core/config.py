from pathlib import Path
from dotenv import load_dotenv
import os

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from backend/
load_dotenv(BASE_DIR.parent / ".env")

# ML Model
MODEL_NAME = "house_model.joblib"
MODEL_PATH = BASE_DIR / "ml" / "house_model.joblib"

# Prediction Settings
PRICE_MULTIPLIER = int(
    os.getenv("PRICE_MULTIPLIER", "100000")
)

AVERAGE_ERROR = int(
    os.getenv("AVERAGE_ERROR", "39000")
)

# API Information
APP_NAME = os.getenv("APP_NAME", "California House Prediction API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

# API Authentication

API_KEY = os.getenv("API_KEY")

# Database
DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "prediction.db"
)
DATABASE_PATH = BASE_DIR.parent / "data" / DATABASE_NAME

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"