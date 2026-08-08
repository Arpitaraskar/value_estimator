def test_prediction(test_client):

    house_data = {
        "MedInc": 1,
        "HouseAge": 0,
        "AveRooms": 1,
        "AveBedrms": 1,
        "Population": 1,
        "AveOccup": 1,
        "Latitude": 32,
        "Longitude": -125
    }

    response = test_client.post(
        "/predict",
        json=house_data
    )

    assert response.status_code == 200

    assert "predicted_price" in response.json()
    assert "predicted_price_short" in response.json()
    assert "confidence_range" in response.json()