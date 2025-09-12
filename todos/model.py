from pydantic import BaseModel, Field
from typing import List

#컨트롤러 모델
class Todo(BaseModel):
    id: int = Field(example=1)
    item: str = Field(example="Example Schema")

class TodoItem(BaseModel):
    item: str = Field(example="Read the next chapter of the book")

#HTTP 응답 모델
class TodoItems(BaseModel):
    todos: List[TodoItem] = Field(
        examples=[
            [
                {"id": 1, "item": "Python 공부하기"},
                {"id": 2, "item": "FastAPI 프로젝트 시작"},
                {"id": 3, "item": "운동하기"}
            ]
        ]
    )
