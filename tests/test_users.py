from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/", json={"name": "Abdul Lasun", "email": "lasun1011@gmail.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Abdul Lasun"
    assert response.json()["email"] == "lasun1011@gmail.com"
    assert "id" in response.json()
    assert response.json()["is_active"] is True


def test_get_user():
    create_response = client.post(
        "/users/", json={"name": "Abdul Lasun", "email": "lasun1011@gmail.com"})
    user_id = create_response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Abdul Lasun"


def test_deactivate_user():
    create_response = client.post(
        "/users/", json={"name": "Abdul Lasun", "email": "lasun1011@gmail.com"})
    user_id = create_response.json()["id"]

    deactivate_response = client.put(f"/users/{user_id}/deactivate")
    assert deactivate_response.status_code == 200
    assert deactivate_response.json() == {"message": "User deactivated"}

    get_response = client.get(f"/users/{user_id}")
    assert get_response.json()["is_active"] is False
