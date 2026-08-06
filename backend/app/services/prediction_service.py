from sqlalchemy.orm import Session

from app.database.models import Prediction
from app.repository.prediction_repository import save_prediction
from fastapi import HTTPException
from app.ml.predictor import predict_price
from app.core.config import PRICE_MULTIPLIER, AVERAGE_ERROR
from app.core.logger import logger

import time


def predict_house_price(db:Session,house):

    # Convert the HouseFeatures object into a normal Python dictionary
    house_data = house.model_dump()

    try:

        logger.info("Prediction request received")


        start_time = time.time()


       


        # Send house data to the ML model &&  #it accept one input called house which contain all house details(like area ,bathroom,bedroom)&& and send house  data to the AI model
        prediction = predict_price(house_data)

        # Convert model prediction into actual USD price
        price_usd = round(prediction * PRICE_MULTIPLIER)

        prediction_record = Prediction(
    MedInc=house.MedInc,
    HouseAge=house.HouseAge,
    AveRooms=house.AveRooms,
    AveBedrms=house.AveBedrms,
    Population=house.Population,
    AveOccup=house.AveOccup,
    Latitude=house.Latitude,
    Longitude=house.Longitude,
    predicted_price=price_usd
)
        save_prediction(db, prediction_record)
        end_time = time.time()

        execution_time = end_time - start_time

        logger.info(
            f"Prediction completed successfully. "
            f"Price: ${price_usd:,.0f} | "
            f"Execution Time: {execution_time:.4f} seconds"
        )

        return {
            "predicted_price": f"${price_usd:,.0f}",
            "predicted_price_short": f"${prediction:.2f} hundred thousand",
            "confidence_range": (
                f"${price_usd - AVERAGE_ERROR:,.0f} "
                f"to ${price_usd + AVERAGE_ERROR:,.0f}"
            )
        }

    except Exception:
        logger.exception("Prediction failed")

        raise HTTPException (
            status_code=500,
            detail="Prediction failed. Please try again later."
        )

        
       