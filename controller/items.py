#controller/items.py
from typing import Union
from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{item_id}")
#item_id: int는 int값이 들어간다는 것을 알려줌/int가 아닌 값이 들어와도 동작함
def read_item(item_id: int,q: Union[str,None] = None):
    return {"itme_id": item_id, "q": q}