from beanie import init_beanie,PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional,Any,List
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict # SettingsConfigDict 임포트 추가
from planner.models.users import User
from planner.models.events import Event

class Database:
    def __init__(self,model):
        self.model = model

    async def save(self,document) -> None:
        await document.create()
        return

    async def get(self,id:PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self,id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.model_dump() #body를 파이썬 dictionary 타입으로 변환
        des_body = {k:v for k,v in des_body.items() if v is not None} #des_body에서 None 제거
        update_query = {"$set": { #mongoDB set query 만듦
            field: value for field,value in
            des_body.items()
        }}

        doc = await self.get(doc_id) #DB에서 해당 id 찾아옴
        if not doc:
            return False
        await doc.update(update_query) #DB 업데이트
        return doc

    async def delete(self,id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

    async def delete_all(self):
        doc = await self.get_all()
        if not doc:
            return False
        await doc.delete_all()
        return True


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    # model_config를 Settings 클래스의 직접적인 멤버로 정의합니다.
    model_config = SettingsConfigDict(env_file=".env")

    async def initalize_database(self):
        print(f"--- Loaded DATABASE_URL: {self.DATABASE_URL} ---")
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[Event, User])