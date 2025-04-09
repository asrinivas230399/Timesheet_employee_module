from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SomeModel(Base):
    __tablename__ = 'some_model'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    # Add other fields as necessary
