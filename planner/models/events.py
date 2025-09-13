from pydantic import BaseModel,Field
from typing import List

class Event(BaseModel):
    id:int #자동 생성 고유 식별자
    title:str =  Field(example="FastAPI Book Launch")#이벤트 타이틀
    image:str = Field(example="https://linktomy.com/image.png")  #이벤트 이미지 배너 링크
    description:str = Field(example="We will be discussing the contents of the FastAPI book in this event. "
                                    "Ensure to com with your own copy to win gifts!")#이벤트 설정
    tags:List[str] = Field(example=["python","fastapi","book","launch"])#그룹화를 위한 이벤트 태그
    location:str = Field(example= "Google Meet") #이벤트 위치