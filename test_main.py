from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_successful_queue_registration():
    response = client.post(
        "/api/v1/queue",
        json={"job_id": "job_999", "payload_matrix": ["token_a", "token_b"]}
    )
    assert response.status_code == 202
    assert response.json()["status"] == "queued"