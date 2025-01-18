from fastapi import APIRouter, HTTPException, status
from schemas.book import BookCreate, Book, BookUpdate
from crud.book_crud import create_book, mark_book_update

book_router = APIRouter()


@book_router.post("/books/", response_model=Book)
def add_book(book: BookCreate):
    try:
        if book(book.id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Book with ID {book.id} already exists."
            )
        return create_book(book)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}")


@book_router.put("/update-book/{book_id}/", response_model=BookUpdate)
def update_book(book_id: int):
    book = mark_book_update(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
