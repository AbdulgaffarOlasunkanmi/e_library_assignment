from fastapi import FastAPI
from routers.user_router import user_router
from routers.book_router import book_router
from routers.borrow_router import borrow_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrow_router, prefix="/borrow_book", tags=["Borrow"])