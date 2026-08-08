def test_invalid_pagination_limit(test_client):

    response = test_client.get(
        "/predictions?skip=0&limit=101"

    )
    assert response.status_code == 422

def test_invalid_pagination_zero_limit(test_client):

    response = test_client.get(
    "/predictions?skip=0&limit=0"
      )
    assert response.status_code == 422

def test_invalid_pagination_negative_skip(test_client):

    response = test_client.get(
         "/predictions?skip=-1&limit=10"
    )
    assert response.status_code == 422
   
