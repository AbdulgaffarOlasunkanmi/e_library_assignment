from database import users_db, books_db, borrow_records_db
from schemas.borrow import CreateBorrowRecord
from datetime import datetime
from typing import List, Optional


def borrow_book(user_id: int, book_id: int) -> Optional[dict]:
    if user_id not in users_db or not users_db[user_id]['is_active']:
        return None
    if book_id not in books_db or not books_db[book_id]['is_available']:
        return None

    borrow_record = CreateBorrowRecord(user_id=user_id, book_id=book_id)
    borrow_record_data = {**borrow_record.dict(),
                          'id': len(borrow_records_db) + 1,
                          'borrow_date': datetime.now(), 'return_date': None}
    borrow_records_db.append(borrow_record_data)

    books_db[book_id]['is_available'] = False
    return borrow_record_data


def return_book(borrow_record_id: int) -> Optional[dict]:
    record = next(
        (record for record in borrow_records_db
         if record['id'] == borrow_record_id), None)
    if record:
        record['return_date'] = datetime.now()
        books_db[record['book_id']]['is_available'] = True
        return record
    return None


def get_user_borrow_records(user_id: int) -> List[dict]:
    return [record for record in borrow_records_db
            if record['user_id'] == user_id]


def get_all_borrow_records() -> List[dict]:
    return borrow_records_db
