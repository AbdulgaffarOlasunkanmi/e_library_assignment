from fastapi import APIRouter, HTTPException
from typing import List
from schemas.borrow import CreateBorrowRecord, BorrowRecord
from crud.borrow_crud import borrow_book, return_book, get_user_borrow_records, get_all_borrow_records

borrow_router = APIRouter()


@borrow_router.post("/borrow/", response_model=BorrowRecord)
def borrow(book: CreateBorrowRecord):
    record = borrow_book(book.user_id, book.book_id)
    if not record:
        raise HTTPException(status_code=400, detail="Cannot borrow book")
    return record


@borrow_router.post("/return/{borrow_record_id}", response_model=BorrowRecord)
def return_borrowed_book(borrow_record_id: int):
    record = return_book(borrow_record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    return record


@borrow_router.get("/user/{user_id}/records", response_model=List[BorrowRecord])
def get_borrow_records(user_id: int):
    return get_user_borrow_records(user_id)


@borrow_router.get("/borrow/records", response_model=List[BorrowRecord])
def get_all_borrow_records_route():
    return get_all_borrow_records()
