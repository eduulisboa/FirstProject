from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class TransactionSchema(BaseModel):
    id: int
    user_id: int
    category: str
    description: str
    cost: Decimal
    created_at: datetime
    updated_at: datetime


class TransactionCreateSchema(BaseModel):
    user_id: int
    category: str
    description: str
    cost: Decimal
