from datetime import datetime

from pydantic import BaseModel


class TransactionSchema(BaseModel):
    id: int
    full_name: str
    email: str
    phone_number: str
    created_at: datetime
    updated_at: datetime


class TransactionCreateSchema(BaseModel):
    full_name: str
    phone_number: str
    email: str
