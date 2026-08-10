from unittest.mock import patch


# mocking testing
@patch("app.services.prediction_service.predict_price")
def test_predict_success(mock_predict, sample_house, test_client):

    mock_predict.return_value = 3.25

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

    mock_predict.assert_called_once_with(expected_house_data)


# failure test
@patch("app.services.prediction_service.predict_price")
def test_predict_model_failure(mock_predict, test_client):

    # Simulate ML model crashing
    mock_predict.side_effect = Exception("Model crashed")

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

    # API should return Internal Server Error
    assert response.status_code == 500

    data = response.json()

    assert data["detail"] == "Prediction failed. Please try again later."

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