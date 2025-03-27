# Event Management API

This project is a FastAPI-based event management system built using a clear structure. It lets you create and update events, register attendees (with email uniqueness enforced), list events, list attendees, and check-in attendees.

## Features

- **Event Management:** Create and update events with details such as name, description, start/end times, location, maximum attendees, and event status.
- **Attendee Registration:** Register attendees for events while enforcing a unique email constraint.
- **Listing & Check-In:** Retrieve lists of events and attendees, and allow attendee check-ins.
- **MVC-Like Structure:** Organized code into models, schemas, controllers, and views (FastAPI routes) for improved maintainability and scalability.

## Project Structure

```
project/
│
├── main.py             # Entry point for the FastAPI app and route definitions.
├── controllers.py      # Business logic and database operations for events and attendees.
├── models.py           # SQLAlchemy ORM models (Event, Attendee, and EventStatus enum).
├── schemas.py          # Pydantic models for request validation and response serialization.
└── database.py         # Database setup (engine, session, and base).
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Shivang-stack/EventManagementAPIs
   cd EventManagementAPIs
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *Dependencies include FastAPI, SQLAlchemy, Pydantic, and Uvicorn.*

4. **Database Initialization:**

   The database is automatically initialized when you start the app. It uses SQLite and creates a file named `events.db` in the project directory.

## Running the Application

To start the FastAPI application, run:

```bash
uvicorn main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000). You can also explore the interactive documentation provided by FastAPI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Error Handling

The project handles common errors gracefully:
- **Unique Constraint Violations:** When trying to register an attendee with an email that already exists for an event, the API returns a clear error message.
- **Not Found Errors:** The API returns appropriate 404 errors when an event or attendee isn’t found.

## Structure

- **Models (models.py):**  
  Defines the ORM models and enums (Event, Attendee, EventStatus).

- **Schemas (schemas.py):**  
  Contains Pydantic models for validating incoming requests and serializing responses (with `orm_mode` and `from_attributes` enabled).

- **Controllers (controllers.py):**  
  Implements the business logic and database interactions for each feature.

- **Views/Routes (main.py):**  
  Maps HTTP endpoints to controller functions, acting as the view layer of the application.

