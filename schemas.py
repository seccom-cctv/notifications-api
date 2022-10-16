from typing import Union
from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    contact_preference: str
    email: str
    phone_number: int


class UserCreate(UserBase):
    pass