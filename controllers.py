from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from models import Event, Attendee, EventStatus
from schemas import EventCreate, EventUpdate, AttendeeRegister

def create_event(event: EventCreate, db: Session):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {"message": "Event created successfully", "event": db_event}

def update_event(event_id: int, event: EventUpdate, db: Session):
    db_event = db.query(Event).filter(Event.event_id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event.dict(exclude_unset=True).items():
        setattr(db_event, key, value)
    db.commit()
    return {"message": "Event updated successfully"}

def register_attendee(event_id: int, attendee: AttendeeRegister, db: Session):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if db.query(Attendee).filter(Attendee.event_id == event_id).count() >= event.max_attendees:
        raise HTTPException(status_code=400, detail="Max attendees limit reached")
    db_attendee = Attendee(**attendee.dict(), event_id=event_id)
    db.add(db_attendee)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        # Check if it's an email uniqueness issue or a different integrity error
        if "UNIQUE constraint failed: attendees.email" in str(e.orig):
            raise HTTPException(status_code=400, detail="Email already registered")
        else:
            raise HTTPException(status_code=400, detail="Integrity error occurred")
    return {"message": "Attendee registered successfully"}
def list_events(status: Optional[EventStatus], db: Session):
    query = db.query(Event)
    if status:
        query = query.filter(Event.status == status)
    return query.all()

def list_attendees(event_id: int, db: Session):
    return db.query(Attendee).filter(Attendee.event_id == event_id).all()

def check_in_attendee(event_id: int, attendee_id: int, db: Session):
    attendee = db.query(Attendee).filter(Attendee.attendee_id == attendee_id, Attendee.event_id == event_id).first()
    if not attendee:
        raise HTTPException(status_code=404, detail="Attendee not found")
    attendee.check_in_status = True
    db.commit()
    return {"message": "Attendee checked in successfully"}
