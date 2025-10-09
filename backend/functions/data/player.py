# Import dependencies
from ..data_schemas import player_data_columns
from .fpl_api_client import FPLApiClient
import pandas as pd

class PlayerData:
    """
    """
    def __init__(self):
        """
        """
        self.client = FPLApiClient()

    def get_player_dataframe(self):
        """
        """
        json = self.client.get_json("bootstrap-static")

        # Create dataframe from endpoint components
        elements_df = pd.DataFrame(json['elements'])
        elements_types_df = pd.DataFrame(json['element_types'])
        teams_df = pd.DataFrame(json['teams'])

        # List of variables to store in dataframe
        player_stats_of_interest = player_data_columns

        # Transform dataframe
        slim_elements_df = elements_df[player_stats_of_interest]
        slim_elements_df['position'] = slim_elements_df.element_type \
            .map(elements_types_df.set_index('id').singular_name)
        slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
        slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
        slim_elements_df['now_cost'] = slim_elements_df['now_cost'].div(10)

        # Add position variable to columns needed in final dataframe
        player_stats_of_interest.append('position')

        # Filter dataset
        slim_elements_df = slim_elements_df[player_stats_of_interest]

        return slim_elements_df.set_index('id')
