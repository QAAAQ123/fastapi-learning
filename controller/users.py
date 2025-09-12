#controller/users.py

from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{user_id}")
#item_id: int는 int값이 들어간다는 것을 알려줌/int가 아닌 값이 들어와도 동작함
def read_user(user_id: int):
    return {"user_id": user_id}