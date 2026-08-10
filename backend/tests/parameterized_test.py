import pytest
from unittest.mock import patch


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


@pytest.mark.parametrize(
    "income",
    [1, 3, 5]
)
@patch("app.services.prediction_service.predict_price")
def test_predict_different_income(
    mock_predict,
    sample_house,
    income,
    test_client
):

    # Mock ML model prediction
    mock_predict.return_value = 3.25

    # Create a copy so fixture is not modified
    test_house = sample_house.copy()

    # Change only income
    test_house["MedInc"] = income

    # Call API
    response = test_client.post(
        "/predict",
        json=test_house
    )

    # Response should be successful
    assert response.status_code == 200

    data = response.json()

    # Check response
    assert data["predicted_price"] == "$325,000"

    # Verify the mock received the correct data
    mock_predict.assert_called_once_with(test_house)