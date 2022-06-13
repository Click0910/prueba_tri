from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(alias='_id')
    user_dni: str
    name: str
    email: str
    password: str
