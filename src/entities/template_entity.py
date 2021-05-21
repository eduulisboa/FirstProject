from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.repositories.postgres.sqlalchemy import Base


class TemplateEntity(Base):
    __tablename__ = "template"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    anything = Column(String(255), index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
