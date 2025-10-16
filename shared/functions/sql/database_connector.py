# Import dependencies
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from ..variables import Variables
import sqlalchemy.orm.session

class DatabaseConnector:
    """
    Handles database connection setup and provides access to the SQLAlchemy
    engine and session factory.
    """
    def __init__(self, source: str = "backend") -> None:
        """
        Initializes the database connector by:
          - Loading environment variables.
          - Reading the DATABASE_URL value.
          - Creating a SQLAlchemy engine and session factory.

        Raises:
            ValueError: If DATABASE_URL is not defined in the environment.
        """
        # Read in environmental variables
        self.vars = Variables(source=source)

        # Define database URL variable and handle issues if value does not exist
        if not self.vars.database_connection_string:
            raise ValueError("database_connection_string not found in environment variables")

        # Create SQLAlchemy engine and session factory
        self.engine = create_engine(self.vars.database_connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def get_engine(self) -> Engine:
        """
        Returns the SQLAlchemy engine object used for executing
        raw SQL queries or DataFrame operations.

        Returns:
            sqlalchemy.engine.Engine: The SQLAlchemy engine instance.
        """
        return self.engine

    def get_session(self) -> sqlalchemy.orm.session:
        """
        Creates and returns a new SQLAlchemy session for ORM operations.

        Returns:
            sqlalchemy.orm.Session: A new database session.
        """
        return self.Session()
