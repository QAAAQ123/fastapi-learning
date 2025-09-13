from fastapi import FastAPI
from starlette.responses import RedirectResponse
from planner.routes.users import user_router
from planner.routes.events import event_router
from planner.database.connection import conn
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    #Load DB
    conn()
    yield
    #close DB
    print("DB Connection ended")

app = FastAPI(lifespan=lifespan)

app.include_router(user_router,prefix="/user")
app.include_router(event_router,prefix="/event")

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")
