from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PredictionResponse(BaseModel):
    id: int
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float
    predicted_price: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PredictionResult(BaseModel):
    predicted_price: str
    predicted_price_short: str
    confidence_range: str