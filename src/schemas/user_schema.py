from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    full_name: str
    email: str
    phone_number: str
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    full_name: str
    phone_number: int
    email: str
