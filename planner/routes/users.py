from fastapi import APIRouter,HTTPException,status
from planner.models.users import User,UserSignIn
from planner.database.connection import Database

user_router = APIRouter(
    tags=["User"]
)

user_database = Database(User)

users = {} #Dictionary타입 set은 set()으로 초기화 해야함

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
           status_code=status.HTTP_409_CONFLICT,
           detail="User with email provided exists already"
        )
    await user_database.save(user)
    return {
        "message": "User created successfully"
    }

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    if user_exist.password == user.password:
        return {
            "message" : "User signed in successfully"
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed"
    )