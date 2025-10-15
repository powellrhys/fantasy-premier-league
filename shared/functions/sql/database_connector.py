# backend/db/database_connector.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class DatabaseConnector:
    """
    Handles DB connection setup and engine/session creation
    """
    def __init__(self):
        """
        """
        # Read in environmental variables
        load_dotenv()

        # Define database url variable and handle issues if value does not exist
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            raise ValueError("DATABASE_URL not found in environment variables")

        # Create sql engine and session
        self.engine = create_engine(self.database_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_engine(self):
        """
        """
        return self.engine

    def get_session(self):
        """
        Returns a new SQLAlchemy session (for ORM use).
        """
        return self.Session()
