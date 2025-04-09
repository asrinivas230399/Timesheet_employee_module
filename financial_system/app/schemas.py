from pydantic import BaseModel
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    currency: str
    timestamp: datetime
    description: str = None

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
