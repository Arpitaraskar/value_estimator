from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch


def test_missing_api_key():

    client = TestClient(app)

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

    assert response.status_code == 401


def test_invalid_api_key():

    client = TestClient(app)

    client.headers.update({
        "X-API-Key": "wrong-key"
    })

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

    assert response.status_code == 401


@patch("app.services.prediction_service.predict_price")
def test_valid_api_key(mock_predict, test_client, sample_house):

    mock_predict.return_value = 2.5

    response = test_client.post(
        "/predict",
        json=sample_house
    )

    assert response.status_code == 200