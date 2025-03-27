from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import engine, Base, get_db
from models import Event, Attendee, EventStatus
from schemas import EventCreate, EventUpdate, AttendeeRegister, EventResponse, AttendeeResponse
import controllers

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/events/", response_model=dict)
def create_event_api(event: EventCreate, db: Session = Depends(get_db)):
    # Return dict with event as EventResponse model
    result = controllers.create_event(event, db)
    # Manually serialize event using EventResponse
    result["event"] = EventResponse.from_orm(result["event"])
    return result

@app.put("/events/{event_id}", response_model=dict)
def update_event_api(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    return controllers.update_event(event_id, event, db)

@app.post("/events/{event_id}/attendees", response_model=dict)
def register_attendee_api(event_id: int, attendee: AttendeeRegister, db: Session = Depends(get_db)):
    return controllers.register_attendee(event_id, attendee, db)

@app.get("/events/", response_model=List[EventResponse])
def list_events_api(status: Optional[EventStatus] = None, db: Session = Depends(get_db)):
    events = controllers.list_events(status, db)
    return [EventResponse.from_orm(event) for event in events]

@app.get("/events/{event_id}/attendees", response_model=List[AttendeeResponse])
def list_attendees_api(event_id: int, db: Session = Depends(get_db)):
    attendees = controllers.list_attendees(event_id, db)
    return [AttendeeResponse.from_orm(attendee) for attendee in attendees]

@app.post("/events/{event_id}/checkin/{attendee_id}", response_model=dict)
def check_in_attendee_api(event_id: int, attendee_id: int, db: Session = Depends(get_db)):
    return controllers.check_in_attendee(event_id, attendee_id, db)
