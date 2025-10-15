# Import dependencies
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

class DatabaseConnector:
    """
    Handles database connection setup and provides access to the SQLAlchemy
    engine and session factory.
    """
    def __init__(self) -> None:
        """
        Initializes the database connector by:
          - Loading environment variables.
          - Reading the DATABASE_URL value.
          - Creating a SQLAlchemy engine and session factory.

        Raises:
            ValueError: If DATABASE_URL is not defined in the environment.
        """
        # Read in environmental variables
        load_dotenv()

        # Define database URL variable and handle issues if value does not exist
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            raise ValueError("DATABASE_URL not found in environment variables")

        # Create SQLAlchemy engine and session factory
        self.engine = create_engine(self.database_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_engine(self) -> Engine:
        """
        Returns the SQLAlchemy engine object used for executing
        raw SQL queries or DataFrame operations.

        Returns:
            sqlalchemy.engine.Engine: The SQLAlchemy engine instance.
        """
        return self.engine

    def get_session(self) -> sessionmaker:
        """
        Creates and returns a new SQLAlchemy session for ORM operations.

        Returns:
            sqlalchemy.orm.Session: A new database session.
        """
        return self.Session()
