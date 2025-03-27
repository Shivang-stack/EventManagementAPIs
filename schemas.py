from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from models import EventStatus

# Request Schemas
class EventCreate(BaseModel):
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    max_attendees: int

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[EventStatus] = None

class AttendeeRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str

# Response Schemas
class EventResponse(BaseModel):
    event_id: int
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    max_attendees: int
    status: EventStatus

    class Config:
        orm_mode = True
        from_attributes = True

class AttendeeResponse(BaseModel):
    attendee_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    event_id: int
    check_in_status: bool

    class Config:
        orm_mode = True
        from_attributes = True
