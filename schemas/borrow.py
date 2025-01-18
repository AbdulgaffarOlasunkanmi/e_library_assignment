from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BorrowRecord(BaseModel):
    id: int


user_id: int
book_id: int
borrow_date: datetime
return_date: Optional[datetime]


class CreateBorrowRecord(BaseModel):
    user_id: int
    book_id: int
