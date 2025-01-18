from database import users_db
from schemas.user import UserCreate


def create_user(user: UserCreate) -> dict:
    user_id = len(users_db) + 1
    users_db[user_id] = {**user.dict(), 'id': user_id, 'is_active': True}
    return users_db[user_id]


def update_user(user_id: int) -> dict:
    if user_id in users_db:
        users_db[user_id]['is_active'] = False
        return users_db[user_id]
    return {}
