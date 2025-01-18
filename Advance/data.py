import os
from sqlmodel import Field, SQLModel, create_engine, Session


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


class HeroId(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=55)
    last_name: str = Field(max_length=55)
    email: str = Field(max_length=55, unique=True)


def insert_data(name: str, secret_name: str, age: int = None):
    hero = Hero(name=name, secret_name=secret_name, age=age)
    session = Session(engine)
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero.id

database_name = "herodata.db"
db_url = f"sqlite:///{database_name}"
engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)


