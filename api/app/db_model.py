from sqlmodel import Field, SQLModel, create_engine
from datetime import date

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key =True)
    title: str = Field(index=True)
    genre: str = Field(index=True)
    media_type: str
    director: str
    starring: str
    release_date: date
    rating: float = Field(ge=0, le=10)

sqlite_file_name = 'database.db'

sqlite_url =f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()