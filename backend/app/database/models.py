from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime

from app.database.db import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    MedInc = Column(Float, nullable=False)
    HouseAge = Column(Float, nullable=False)
    AveRooms = Column(Float, nullable=False)
    AveBedrms = Column(Float, nullable=False)
    Population = Column(Float, nullable=False)
    AveOccup = Column(Float, nullable=False)
    Latitude = Column(Float, nullable=False)
    Longitude = Column(Float, nullable=False)


    predicted_price = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)