from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.settings import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database():
    database = Session()
    try:
        yield database
    finally:
        database.close()


def create_database():
    Base.metadata.create_all(bind=engine)
