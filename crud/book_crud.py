from database import books_db
from schemas.book import BookCreate


def create_book(book: BookCreate) -> dict:
    book_id = len(books_db) + 1
    books_db[book_id] = {**book.dict(), 'id': book_id, 'is_available': True}
    return books_db[book_id]


def mark_book_update(book_id: int) -> dict:
    if book_id in books_db:
        books_db[book_id]['is_available'] = False
    return books_db[book_id]
    return {}
