from sqlalchemy.orm import Session

from app.database.models import Prediction

def save_prediction(db: Session, prediction: Prediction):
    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction