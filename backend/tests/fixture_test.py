import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

#fixture testing 

@pytest.fixture
def sample_house():
    return {
        "MedInc": 1,
        "HouseAge": 10,
        "AveRooms": 5,
        "AveBedrms": 1,
        "Population": 100,
        "AveOccup": 2,
        "Latitude": 34,
        "Longitude": -118
    }

@patch("app.services.prediction_service.predict_price")
def test_predict_success(mock_predict, sample_house):

    mock_predict.return_value = 3.25

    response = client.post(
        "/predict",
        json=sample_house
    )

    assert response.status_code == 200

    data = response.json()

    assert data["predicted_price"] == "$325,000"

    mock_predict.assert_called_once_with(sample_house)