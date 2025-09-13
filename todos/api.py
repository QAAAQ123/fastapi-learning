from fastapi import FastAPI

from todos.todo import todo_router
pratice_app = FastAPI()

@pratice_app.get("/")
async def welcome() -> dict: 
    return {
            "message":"Hello"
    }

pratice_app.include_router(todo_router)