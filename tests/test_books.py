from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/", json={"title": "Python Lesson", "author": "Abdul-Lasun"})
    assert response.status_code == 200
    assert response.json()["title"] == "Book Title"
    assert response.json()["author"] == "Book Author"
    assert "id" in response.json()
    assert response.json()["is_available"] is True


def test_mark_book_unavailable():
    create_response = client.post(
        "/books/", json={"title": "Python Book", "author": "Abdul-gaffar"})
    book_id = create_response.json()["id"]

    unavailable_response = client.put(f"/books/{book_id}/unavailable")
    assert unavailable_response.status_code == 200
    assert unavailable_response.json(
    ) == {"message": "Book marked as unavailable"}

    get_response = client.get(f"/books/{book_id}")
    assert get_response.json()["is_available"] is False
