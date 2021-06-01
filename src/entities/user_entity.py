from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.repositories.postgres.sqlalchemy import Base


class UserEntity(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255), index=True)
    phone_number = Column(String(16))
    email = Column(String(225))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    transaction = relationship("TransactionEntity", back_populates="owner")
