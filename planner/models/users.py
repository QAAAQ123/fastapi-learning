from pydantic import BaseModel,EmailStr,Field
from typing import List,Optional
from planner.models.events import Event

class User(BaseModel):
    email: EmailStr = Field(example="fastap@packt.com") #사용자 이메일
    password: str = Field(example="strong!!!") #사용자 패스워드
    events: Optional[List[Event]] = Field(example=[]) #해당 사용자가 생성한 이벤트, 처음에는 비어있다

class UserSignIn(BaseModel):
    email: EmailStr = Field(example="fastap@packt.com")
    password: str = Field(example="strong!!!")
