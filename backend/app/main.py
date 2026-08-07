from fastapi import FastAPI
from app.core.config import APP_NAME, APP_VERSION
from app.database.db import init_db
from app.api.prediction_routes import router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

init_db()

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "House Prediction API is running"
    }

@app.get("/health")
def health():
    return{
       "status": "healthy"
    }