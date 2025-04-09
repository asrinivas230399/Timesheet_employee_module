from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    access_level = Column(String)

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name}, role={self.role}, access_level={self.access_level})"