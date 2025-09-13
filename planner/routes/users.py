from fastapi import APIRouter,HTTPException,status
from planner.models.users import User,UserSignIn

user_router = APIRouter(
    tags=["User"]
)
users = {} #Dictionary타입 set은 set()으로 초기화 해야함

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username esixts"
        )
    users[data.email] = data
    return {
        "message" : "User successfully registered!"
    }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    return {
        "message": "User signed in successfully"
    }