import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["application"] == "student-ml-api"
    assert data["application_version"] == "1.1.0"
    assert data["model_version"] == "model-1"

def test_predict_success(client):
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    data = response.get_json()
    assert data["input"] == 10
    assert data["prediction"] == 20

def test_predict_missing_input(client):
    response = client.post("/predict", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_predict_invalid_input(client):
    response = client.post("/predict", json={"value": "not-a-number"})
    assert response.status_code == 400
    assert "error" in response.get_json()
