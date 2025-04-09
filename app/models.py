from sqlalchemy import Column, Integer, String
from .database import Base

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    position = Column(String, index=True)
    salary = Column(Integer)
    version = Column(Integer, nullable=False, default=0)

    __mapper_args__ = {
        "version_id_col": version,
        "version_id_generator": False
    }

    def calculate_annual_cost(self):
        return self.salary * 12