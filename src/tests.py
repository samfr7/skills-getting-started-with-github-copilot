# Let's use the AAA (Arrange-Act-Assert) testing pattern to structure our tests

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
def test_get_activities():
    # Arrange - No setup needed for this test

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data
    assert "Art Club" in data
    assert "Music Class" in data