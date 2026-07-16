from fastapi.testclient import TestClient

from src import app as app_module


def test_unregister_participant_removes_the_email_from_activity():
    client = TestClient(app_module.app)
    activity_name = "Chess Club"
    app_module.activities[activity_name]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    response = client.delete(
        f"/activities/{activity_name}/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    assert "michael@mergington.edu" not in app_module.activities[activity_name]["participants"]
    assert "daniel@mergington.edu" in app_module.activities[activity_name]["participants"]
