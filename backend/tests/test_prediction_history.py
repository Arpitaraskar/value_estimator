def test_prediction_history(test_client):

    response   = test_client.get(
        "/predictions?skip=0&limit=10"
    )

    assert response.status_code == 200
    assert isinstance(response.json(),list)