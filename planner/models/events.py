from beanie import Document
from typing import Optional,List
from pydantic import BaseModel


class Event(Document):
    creator: Optional[str]
    title:str #이벤트 타이틀
    image:str  #이벤트 이미지 배너 링크
    description:str#이벤트 설정
    tags:List[str] #그룹화를 위한 이벤트 태그
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

    class Settings:
        name = "events"

class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

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