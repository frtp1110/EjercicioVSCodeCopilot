from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_remove_participant_from_activity():
    response = client.delete(
        "/activities/Chess%20Club/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"

    activities_response = client.get("/activities")
    activities = activities_response.json()["Chess Club"]
    assert "michael@mergington.edu" not in activities["participants"]
