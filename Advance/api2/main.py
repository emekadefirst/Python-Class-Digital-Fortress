from fastapi import FastAPI, Request, status
from pydantic import BaseModel


class Event(BaseModel):
    id : int
    title: str
    date: str


app = FastAPI(
    title="15th Feb 2025",
    version="0.0.1",
    description="API for managing events",
)


@app.post("/events/create")
def create(event: Event):
    return {
        "status": status.HTTP_201_CREATED,
        "message": "Event created successfully",
        "data": {
            "id": event.id,
            "title": event.title,
            "date": event.date,
        }
    }

@app.delete("/events/delete/{id}")
def delete_event(id: int):
    return {
        "status": status.HTTP_200_OK,
        "message": f"Event with id {id} deleted successfully",
    }

@app.get("/")
def main(request: Request):
    user_ip = request.client.host
    return {"message": "Welcome to the Event API", "ip": user_ip}

event = [
    {"id": 1, "title": "Birthday Party", "date": "2025-02-15"},
    {"id": 2, "title": "Conference", "date": "2025-02-17"},
    {"id": 3, "title": "Meeting", "date": "2025-02-18"},
    {"id": 4, "title": "Workshop", "date": "2025-02-20"},
    {"id": 5, "title": "Vacation", "date": "2025-02-25"},
]

@app.get("/events")
def events():
    return event


@app.get("events/{id}")
def get_event(id: int):
    return event[id]
