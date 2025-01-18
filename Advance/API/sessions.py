from sqlmodel import Session, select
from models import engine, User


def create_user(username):
    try:
        with Session(engine) as session:
            user = User(username=username)
            session.add(user)
            session.commit()
            data = {"id": user.id, "username": user.username}
            return data
    except Exception as e:
        return e

def all_user():
    try:
        with Session(engine) as session:
            users = select(User)
            response = session.exec(users)
            return response.all()
    except Exception as e:
        return e

def get_or_404(id):
    try:
        with Session(engine) as session:
            user = select(User).where(User.id == id)
            response = session.exec(user)
            return response.all()
    except Exception as e:
        return e


def update(id, new_username):
    try:
        with Session(engine) as session:
            user = select(User).where(User.id == id)
            response = session.exec(user)
            data = response.one()
            data.username = new_username
            session.add(data)
            session.commit()
            return data
    except Exception as e:
        return e


def delete(id):
    try:
        with Session(engine) as session:
            user = select(User).where(User.id == id)
            response = session.exec(user)
            response.all()
            session.delete(response)
            session.commit()
            return "User deleted"
    except Exception as e:
        return e
