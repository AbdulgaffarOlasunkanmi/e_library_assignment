from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_borrow_book():
    user_response = client.post(
        "/users/", json={"name": "Abdul Lasun", "email": "lasun1011@gmail.com"})
    user_id = user_response.json()["id"]

    book_response = client.post(
        "/books/", json={"title": "Python Book", "author": "Abdul-gaffar"})
    book_id = book_response.json()["id"]

    borrow_response = client.post(
        "/borrow/borrow", json={"user_id": user_id, "book_id": book_id, "borrow_date": "2024-12-23"})
    assert borrow_response.status_code == 200
    assert borrow_response.json()["user_id"] == user_id
    assert borrow_response.json()["book_id"] == book_id

    book_response = client.get(f"/books/{book_id}")
    assert book_response.json()["is_available"] is False


def test_return_book():
    user_response = client.post(
        "/users/", json={"name": "Abdul Lasun", "email": "lasun1011@gmail.com"})
    user_id = user_response.json()["id"]

    book_response = client.post(
        "/books/", json={"title": "Python Book", "author": "Abdul-gaffar"})
    book_id = book_response.json()["id"]

    borrow_response = client.post(
        "/borrow/borrow", json={"user_id": user_id, "book_id": book_id, "borrow_date": "2024-12-23"})
    borrow_id = borrow_response.json()["id"]

    return_response = client.post(f"/borrow/return/{borrow_id}")
    assert return_response.status_code == 200
    assert return_response.json()["return_date"] is not None

    book_response = client.get(f"/books/{book_id}")
    assert book_response.json()["is_available"] is True
