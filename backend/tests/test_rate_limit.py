def test_rate_limit(test_client, sample_house):
    responses = []

    for _ in range(21):
        response = test_client.post("/predict", json=sample_house)
        responses.append(response.status_code)

    assert responses[-1] == 429