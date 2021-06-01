from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.repositories.postgres.sqlalchemy import Base


class TransactionEntity(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    category = Column(String(255))
    description = Column(String(255))
    cost = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    owner = relationship("UserEntity", back_populates="transaction")
