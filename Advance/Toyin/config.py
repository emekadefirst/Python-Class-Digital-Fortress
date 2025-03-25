from sqlmodel import Field, SQLModel, create_engine

database_name = "Toyin.db"

db_url = f"sqlite:///{database_name}"
engine = create_engine(db_url, echo=True)


# Code below omitted 👇