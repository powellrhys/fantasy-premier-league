# Import dependencies
from .database_connector import DatabaseConnector
from database.models import PlayerOverview
import pandas as pd


class PlayerRepository:
    """
    Provides methods to read and write data for the 'player_overview' table.
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
        Writes player overview data from a pandas DataFrame to the
        'player_overview' table.

        Args:
            df (pd.DataFrame): DataFrame containing player overview data.
            if_exists (str, optional): Behavior when the table already exists.
                Options: 'fail', 'replace', or 'append'. Defaults to 'replace'.
        """
        # Write data to sql
        df.to_sql(name="player_overview", con=self.engine, if_exists=if_exists, index=False)

    def read_dataframe(self) -> pd.DataFrame:
        """
        Reads all player overview data from the database into a pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing all rows from the
            'player_overview' table.
        """
        # Define query read data from sql
        query = "SELECT * FROM player_overview"
        return pd.read_sql(query, self.engine)

    def insert_players_orm(self, df: pd.DataFrame) -> None:
        """
        Inserts player overview data using SQLAlchemy ORM for finer control.
        Performs a bulk insert for improved performance.

        Args:
            df (pd.DataFrame): DataFrame containing player overview data
                to insert into the database.
        """
        # Define sql session and write data to sql table
        session = self.Session()
        try:
            players = [PlayerOverview(**row.to_dict()) for _, row in df.iterrows()]
            session.bulk_save_objects(players)
            session.commit()
        finally:
            session.close()
