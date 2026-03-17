from pydantic import BaseModel, Field
from datetime import date


class InputSchema(BaseModel):
    name: str
    genre: str
    media_type: str
    director: str
    starring: str
    date: date
    rating: float = Field(ge=0, le=10)

class OutputSchema(BaseModel):
    
    genre: str
    media_type: str
    director: str
    starring: str
    date: date
    rating: float = Field(ge=0, le=10)
