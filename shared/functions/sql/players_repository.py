# Import dependencies
from .database_connector import DatabaseConnector
from database.models import PlayerOverview
import pandas as pd

class PlayerRepository:
    """
    Handles reading/writing players data.
    """
    def __init__(self, db_connector: DatabaseConnector):
        """
        """
        self.engine = db_connector.get_engine()
        self.Session = db_connector.Session

    def write_dataframe(self, df: pd.DataFrame, if_exists="replace"):
        """
        Writes player data from a DataFrame to the 'player' table.
        """
        df.to_sql(name="player_overview", con=self.engine, if_exists=if_exists, index=False)

    def read_dataframe(self) -> pd.DataFrame:
        """
        Reads all player data as a DataFrame.
        """
        # Define query and read from database table
        query = "SELECT * FROM player_overview"
        return pd.read_sql(query, self.engine)

    def insert_players_orm(self, df: pd.DataFrame):
        """
        Example of writing using ORM for more control.
        """
        session = self.Session()
        try:
            players = [PlayerOverview(**row.to_dict()) for _, row in df.iterrows()]
            session.bulk_save_objects(players)
            session.commit()
        finally:
            session.close()
