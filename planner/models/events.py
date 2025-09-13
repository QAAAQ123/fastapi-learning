from sqlmodel import JSON,SQLModel,Field,Column
from typing import Optional,List

class Event(SQLModel,table=True):
    id:int = Field(default=None,primary_key=True)#자동 생성 고유 식별자
    title:str #이벤트 타이틀
    image:str  #이벤트 이미지 배너 링크
    description:str#이벤트 설정
    tags:List[str] = Field(sa_column=Column(JSON))#그룹화를 위한 이벤트 태그
    location:str #이벤트 위치

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example" : {
                "title": "FastAPI Book Launch",
                "image": "https://linktomy.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event."
                               " Ensure to com with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Gooele Meet"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        json_schema_extra = {
            "example" : {
                "title": "FastAPI Book Launch",
                "image": "https://linktomy.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event."
                               " Ensure to com with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Gooele Meet"
            }
        }