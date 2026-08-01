from fastapi import APIRouter

from app.schemas.house_schema import HouseFeatures
from app.services.prediction_service import predict_house_price

router = APIRouter(
    prefix="",
    tags=["House Prediction"]
)

@router.post("/predict")
def predict(house: HouseFeatures):
    return predict_house_price(house)