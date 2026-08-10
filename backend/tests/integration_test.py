# mock test

from unittest.mock import patch


@patch("app.services.prediction_service.predict_price")
def test_predict_integration(mock_predict, test_client):

    mock_predict.return_value = 2.5

    response = test_client.post(
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

    assert "predicted_price" in data
    assert "predicted_price_short" in data
    assert "confidence_range" in data