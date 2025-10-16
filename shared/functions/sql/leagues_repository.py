# Import dependencies
from .database_connector import DatabaseConnector
from database.models import LeagueOverview
import pandas as pd

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

    def write_dataframe(self, df: pd.DataFrame, if_exists: str = "replace") -> None:
        """
        Writes league overview data from a pandas DataFrame to the
        'league_overview' table.

        Args:
            df (pd.DataFrame): DataFrame containing league overview data.
            if_exists (str, optional): Behavior when the table already exists.
                Options: 'fail', 'replace', or 'append'. Defaults to 'replace'.
        """
        # Write data to sql
        df.to_sql(name="league_overview", con=self.engine, if_exists=if_exists, index=False)

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

    def insert_leagues_orm(self, df: pd.DataFrame) -> None:
        """
        Inserts league overview data using SQLAlchemy ORM for finer control.
        Performs a bulk insert for improved performance.

        Args:
            df (pd.DataFrame): DataFrame containing league overview data
                to insert into the database.
        """
        # Define sql session and write data to sql table
        session = self.Session()
        try:
            leagues = [LeagueOverview(**row) for row in df.to_dict('records')]
            session.bulk_save_objects(leagues)
            session.commit()
        finally:
            session.close()
