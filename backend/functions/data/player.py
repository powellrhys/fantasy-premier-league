# Import dependencies
from ..data_schemas import player_data_columns
from .fpl_api_client import FPLApiClient
import pandas as pd

class PlayerData:
    """
    A class to retrieve and process Fantasy Premier League player data into a DataFrame.
    """

    def __init__(self):
        """
        Initialize the PlayerData instance with an FPL API client.
        """
        self.client = FPLApiClient()

    def get_player_dataframe(self) -> pd.DataFrame:
        """
        Retrieve player data from the FPL API and return it as a processed DataFrame.
        The DataFrame includes selected player stats, position, team, value, and cost.
        """
        # Collect data from bootstrap-static api
        json = self.client.get_json("bootstrap-static")

        # Create dataframes from data
        elements_df = pd.DataFrame(json['elements'])
        elements_types_df = pd.DataFrame(json['element_types'])
        teams_df = pd.DataFrame(json['teams'])

        # Define columns of interest
        player_stats_of_interest = player_data_columns

        # Filter data based on columns
        slim_elements_df = elements_df[player_stats_of_interest]

        # Create new player columns
        slim_elements_df['position'] = slim_elements_df.element_type \
            .map(elements_types_df.set_index('id').singular_name)
        slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
        slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
        slim_elements_df['now_cost'] = slim_elements_df['now_cost'].div(10)

        # Filter data by columns of interest
        player_stats_of_interest.append('position')
        slim_elements_df = slim_elements_df[player_stats_of_interest]

        return slim_elements_df.set_index('id')
