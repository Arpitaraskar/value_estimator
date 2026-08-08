from sqlalchemy.orm import Session

from app.database.models import Prediction

def save_prediction(db: Session, prediction: Prediction):
    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction

def get_predictions(
    db: Session,
    skip: int = 0,
    limit: int = 10
):
    return db.query(Prediction).order_by(
        Prediction.created_at.desc()
    ).offset(skip).limit(limit).all()