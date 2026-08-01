from unittest.mock import patch


   

@patch("app.services.prediction_service.predict_price")
def test_predict_using_conftest(mock_predict, test_client, sample_house):

    mock_predict.return_value = 3.25

    response = test_client.post(
        "/predict",
        json=sample_house
    )

    assert response.status_code == 200

    data = response.json()

    assert data["predicted_price"] == "$325,000"

    mock_predict.assert_called_once_with(sample_house)