from sqlmodel import SQLModel, Field, create_engine


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    
db_name = "api.db"
db_url = f"sqlite:///{db_name}"
engine = create_engine(db_url, echo=True)
SQLModel.metadata.create_all(engine)