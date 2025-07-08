import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

os.environ["BASIC_AUTH_USERNAME"] = "admin"
os.environ["BASIC_AUTH_PASSWORD"] = "secret"
os.environ["SQS_QUEUE_URL"] = "dummy-url"

def test_unauthorized():
    response = client.post("/data", json={"id": "123"})
    assert response.status_code == 401

def test_authorized(monkeypatch):
    def mock_send_message(QueueUrl, MessageBody):
        return {"MessageId": "abc-123"}

    monkeypatch.setattr("boto3.client", lambda x: type("MockSQS", (), {"send_message": mock_send_message})())
    response = client.post("/data", json={"id": "123"}, auth=("admin", "secret"))
    assert response.status_code == 200
    assert response.json()["status"] == "queued"
