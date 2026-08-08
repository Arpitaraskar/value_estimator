from fastapi import FastAPI
from app.core.config import APP_NAME, APP_VERSION
from app.database.db import init_db
from app.api.prediction_routes import router
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.core.rate_limiter import limiter

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)
app.add_middleware(SlowAPIMiddleware)

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