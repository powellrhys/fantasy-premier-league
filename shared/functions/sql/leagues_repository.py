# Import dependencies
from .database_connector import DatabaseConnector
from database.models import LeagueOverview
import pandas as pd


class LeagueRepository:
    """
    Handles reading/writing league overview data.
    """

    def __init__(self, db_connector: DatabaseConnector):
        """
        Initializes the repository with a database connector.
        """
        self.engine = db_connector.get_engine()
        self.Session = db_connector.Session

    def write_dataframe(self, df: pd.DataFrame, if_exists="replace"):
        """
        Writes league overview data from a DataFrame to the 'league_overview' table.
        """
        df.to_sql(name="league_overview", con=self.engine, if_exists=if_exists, index=False)

    def read_dataframe(self) -> pd.DataFrame:
        """
        Reads all league overview data as a DataFrame.
        """
        query = "SELECT * FROM league_overview"
        return pd.read_sql(query, self.engine)

    def insert_leagues_orm(self, df: pd.DataFrame):
        """
        Example of writing using ORM for more control (bulk insert).
        """
        session = self.Session()
        try:
            leagues = [LeagueOverview(**row.to_dict()) for _, row in df.iterrows()]
            session.bulk_save_objects(leagues)
            session.commit()
        finally:
            session.close()
