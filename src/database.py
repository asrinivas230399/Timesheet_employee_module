from sqlalchemy import create_engine, Column, Integer, String, Tuple
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)

class Level(Base):
    __tablename__ = 'levels'

    level_id = Column(Integer, primary_key=True)
    name = Column(String)
    salary_range = Column(Tuple)

def init_db():
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Predefined levels
    predefined_levels = [
        Level(level_id=1, name='Junior', salary_range=(30000, 50000)),
        Level(level_id=2, name='Mid', salary_range=(50000, 70000)),
        Level(level_id=3, name='Senior', salary_range=(70000, 100000)),
    ]

    # Populate the Level table
    for level in predefined_levels:
        session.merge(level)

    session.commit()
    session.close()

    return engine