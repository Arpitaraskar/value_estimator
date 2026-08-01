from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def test_client():
    return client

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