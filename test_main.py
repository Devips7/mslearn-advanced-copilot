from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_cities_spain():
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    # Optionally, check for expected cities if you know them, e.g.:
    # assert "Madrid" in response.json()