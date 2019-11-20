from sqlalchemy import Column, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    first_name = Column(TEXT)
    last_name = Column(TEXT)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
