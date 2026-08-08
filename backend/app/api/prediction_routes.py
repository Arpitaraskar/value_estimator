from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query
from app.database.dependencies import get_db
from app.schemas.house_schema import HouseFeatures
from app.schemas.prediction_schema import PredictionResponse
from app.services.prediction_service import (
    predict_house_price,
    get_prediction_history
)

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

@router.get(
    "/predictions",
    response_model=list[PredictionResponse]
)
def prediction_history(
    skip: int = Query(0,ge=0),
    limit: int =Query(10,ge=1,le=100),
    db: Session = Depends(get_db)
):
    return get_prediction_history(db, skip, limit)