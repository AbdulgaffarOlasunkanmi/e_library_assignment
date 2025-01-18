from fastapi import APIRouter, HTTPException, status
from schemas.user import UserCreate, UserUpdate, User
from crud.user_crud import create_user, update_user

user_router = APIRouter()


@user_router.post("/users/", response_model=User)
def add_user(user: UserCreate):
    try:
        if user(user.id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with the provided ID already exists."
            )
        new_user = create_user(user)
        return new_user
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )


@user_router.put("/users/{user_id}/update", response_model=UserUpdate)
def update_user_account(user_id: int):
    user = update_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
