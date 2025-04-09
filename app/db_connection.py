from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import logging

class DBConnection:
    def __init__(self, database_url: str):
        # Optimize connection pooling
        self.engine = create_engine(database_url, pool_size=20, max_overflow=0)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self) -> Session:
        """
        Provides a new session for database operations.
        """
        return self.SessionLocal()

    def execute_query(self, query):
        """
        Executes a given query and returns the result.
        """
        try:
            with self.get_session() as session:
                result = session.execute(query)
                return result.fetchall()
        except Exception as e:
            logging.error("Error executing query: %s", e)
            return []
