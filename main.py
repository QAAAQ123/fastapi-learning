from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
#item_id: int는 int값이 들어간다는 것을 알려줌/int가 아닌 값이 들어와도 동작함
def read_item(item_id: int,q: Union[str,None] = None):
    return {"itme_id": item_id, "q": q}