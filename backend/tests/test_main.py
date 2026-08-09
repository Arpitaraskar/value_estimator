from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch
import pytest


client = TestClient(app)


#mocking testing
@patch("app.services.prediction_service.predict_price")
def test_predict_success(mock_predict,sample_house):



    mock_predict.return_value = 3.25

  

    response = client.post(
        "/predict",
        json={
            "MedInc": 1,
            "HouseAge": 10,
            "AveRooms": 5,
            "AveBedrms": 1,
            "Population": 100,
            "AveOccup": 2,
            "Latitude": 34,
            "Longitude": -118
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["predicted_price"] == "$325,000"

    expected_house_data = {
    "MedInc": 1,
    "HouseAge": 10,
    "AveRooms": 5,
    "AveBedrms": 1,
    "Population": 100,
    "AveOccup": 2,
    "Latitude": 34,
    "Longitude": -118
}

    # mock_predict.assert_called_once()

    mock_predict.assert_called_once_with(expected_house_data)

##failure test

@patch("app.services.prediction_service.predict_price")
def test_predict_model_failure(mock_predict):

    # Simulate ML model crashing
    mock_predict.side_effect = Exception("Model crashed")

    response = client.post(
        "/predict",
        json={
            "MedInc": 1,
            "HouseAge": 10,
            "AveRooms": 5,
            "AveBedrms": 1,
            "Population": 100,
            "AveOccup": 2,
            "Latitude": 34,
            "Longitude": -118
        }
    )

    # API should return Internal Server Error
    assert response.status_code == 500

    data = response.json()

    # Verify error message
    assert data["detail"] == "Prediction failed. Please try again later."

    # Verify predict_price() was called with correct data
    expected_house_data = {
        "MedInc": 1,
        "HouseAge": 10,
        "AveRooms": 5,
        "AveBedrms": 1,
        "Population": 100,
        "AveOccup": 2,
        "Latitude": 34,
        "Longitude": -118
    }

    mock_predict.assert_called_once_with(expected_house_data)
