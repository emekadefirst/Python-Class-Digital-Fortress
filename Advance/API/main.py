from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from sessions import create_user, all_user, get_or_404, update, delete


class User(BaseModel):
    username: Optional[str]
    
class Update(BaseModel):
    username: Optional[str]


class Message(BaseModel):
    message: str


app = FastAPI(
    title="Anything AI",
    description="This ai does Anything",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "API is working"}


@app.get("/users")
def all_users():
    users = all_user()
    return users


@app.get("/user/{user_id}")
async def read_item(user_id: int):
    user = get_or_404(user_id)
    return user


@app.post("/user/add")
def add_new_user(user: User):
    username = user.username
    user = create_user(username)
    return user


@app.put("/user/update/{user_id}")
def update_user(user_id, data: Update):
        data = update(user_id, data.username)
        return data


@app.delete("/user/delete/{user_id}")
def message(user_id):
    data = delete(user_id)
    return data
