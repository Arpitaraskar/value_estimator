


import joblib
import pandas as pd


from app.core.config import MODEL_PATH




model = joblib.load(MODEL_PATH)


def predict_price(house_data: dict):

    input_df = pd.DataFrame([house_data])

    prediction = model.predict(input_df)[0]

    return prediction