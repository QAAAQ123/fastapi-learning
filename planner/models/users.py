from typing import Optional,List
from beanie import Document,Link
from pydantic import BaseModel,EmailStr
from planner.models.events import Event

class User(Document):
    email: EmailStr #사용자 이메일
    password: str #사용자 패스워드
    events: Optional[List[Event]] = None#해당 사용자가 생성한 이벤트, 처음에는 비어있다

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example" : {
                "email" : "fastap@packt.com",
                "password" : "strong!!!",
                "events" : []
            }
        }


# class UserSignIn(BaseModel):
#     email: EmailStr
#     password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str