from fastapi import APIRouter,HTTPException,status,Body,Depends,Request
from sqlmodel import select

from planner.database.connection import get_session
from planner.models.events import Event,EventUpdate
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.get("/",response_model=List[Event])
async def retrieve_all_event(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}",response_model=Event)
async def retrieve_event(id: int,session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    # for event in events:
    #     if event.id == id:
    #         return event
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.post("/new")
async def create_event(new_event: Event, session = Depends(get_session) ) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message": "Event created successfully"
    }

@event_router.delete("/delete/{id}")
async def delete_evnet(id: int,session = Depends(get_session)) -> dict:
    event = session.get(Event,id)
    if event:
        session.delete(event)
        session.commit()
        return {
            "message":"Event deleted successfully"
        }
    # for event in events:
    #     if event.id == id:
    #         events.remove(event)
    #         return{
    #             "message": "Event deleted successfully"
    #         }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }

@event_router.put("/edit/{id}",response_model=Event)
async def update_event(id: int,new_data: Event,session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.model_dump(exclude_unset=True)
        for key,value in event_data.items():
            setattr(event,key,value)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
