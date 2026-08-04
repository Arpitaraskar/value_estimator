# import joblib
# import pandas as pd

# from app.core.config import MODEL_PATH

# model = joblib.load(MODEL_PATH)


# def predict_price(house_data: dict):

#     input_df = pd.DataFrame([house_data])

#     prediction = model.predict(input_df)[0]

#     return prediction

import joblib
import pandas as pd

from app.core.config import MODEL_PATH

model = None


def load_model():
    global model

    if model is None:
        model = joblib.load(MODEL_PATH)

    return model


def predict_price(house_data: dict):

    loaded_model = load_model()

    input_df = pd.DataFrame([house_data])

    prediction = loaded_model.predict(input_df)[0]

    return prediction