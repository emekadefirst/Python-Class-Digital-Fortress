from sqlmodel import Session
from data import engine, Hero


def insert_data(name: str, secret_name: str, age: int = None):
    hero = Hero(name=name, secret_name=secret_name, age=age)
    session = Session(engine)
    session.add(hero)
    session.commit()
    session.refresh(hero) # optional
    return hero.id

def add_data(name: str, secret_name: str, age: int = None):
    try:
        with Session(engine) as session:
            hero = Hero(name=name, secret_name=secret_name, age=age)  
            session.add(hero)
            session.commit() 
            return hero.id
    except Session as e:
        return "Session not found"


print(add_data("Batman", "Bruce Wayne", 35))        
        
