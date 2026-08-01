from fastapi import FastAPI

from app.api.prediction_routes import router

app = FastAPI(
    title="APP_NAME",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "House Prediction API is running"
    }