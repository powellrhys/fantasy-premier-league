# Import dependencies
from .database_connector import DatabaseConnector
from database.models import LeagueOverview
from sqlalchemy import text
import pandas as pd
import time

class LeagueRepository:
    """
    Provides methods to read and write data for the 'league_overview' table.
    Supports both DataFrame-based operations and ORM-based inserts.
    """
    def __init__(self, db_connector: DatabaseConnector) -> None:
        """
        Initializes the repository with a DatabaseConnector instance.

        Args:
            db_connector (DatabaseConnector): Object providing access to the
                SQLAlchemy engine and session factory.
        """
        self.engine = db_connector.get_engine()
        self.Session = db_connector.Session

    def read_dataframe(self) -> pd.DataFrame:
        """
        Reads all league overview data from the database into a pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing all rows from the
            'league_overview' table.
        """
        # Define query read data from sql
        query = "SELECT * FROM league_overview"
        return pd.read_sql(query, self.engine)

    def append_new_data_to_database(self, df: pd.DataFrame) -> None:
        """
        Safely replaces data in 'league_overview' using a versioned timestamp approach.
        Keeps old data until the new version is fully inserted.
        """
        session = self.Session()
        current_version = int(time.time())

        # Assign the current timestamp to all rows
        df["creation_timestamp"] = current_version

        try:
            # Insert new data with a new version
            session.bulk_save_objects([LeagueOverview(**row) for row in df.to_dict('records')])
            session.commit()

            # Once successful, delete older versions
            session.execute(text(f"DELETE FROM league_overview WHERE creation_timestamp < {current_version}"))
            session.commit()

        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
