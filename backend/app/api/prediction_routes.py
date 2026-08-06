from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.house_schema import HouseFeatures
from app.services.prediction_service import predict_house_price

router = APIRouter(
    prefix="",
    tags=["House Prediction"]
)

@router.post("/predict")
def predict(
    house: HouseFeatures,
    db: Session = Depends(get_db)
):
    return predict_house_price(db, house)