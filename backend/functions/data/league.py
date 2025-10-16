# Import dependencies
from .fpl_api_client import FPLApiClient
from .manager import Manager
import pandas as pd

class League:
    """
    A class to retrieve and organize data for a Fantasy Premier League league.
    """

    def __init__(self, league_id: str):
        """
        Initialize the League with a given league ID.
        """
        self.league_id = league_id
        self.client = FPLApiClient()

    def collect_league_data(self) -> pd.DataFrame:
        """
        Collect and return league standings with chip usage data as a DataFrame.
        """
        data = self.client.get_json(f"leagues-classic/{self.league_id}/standings")
        standings_df = pd.DataFrame(data['standings']['results'])

        # Create chip data
        chip_data = [Manager(entry['entry']).get_chip_flags() for entry in data['standings']['results']]
        chip_df = pd.DataFrame(chip_data)

        # Merge standings with chip flags
        full_df = standings_df.merge(chip_df, on='entry', how='left')
        full_df['league_name'] = data['league']['name']
        full_df.rename(columns={'rank': 'league_rank'}, inplace=True)

        full_df = full_df.drop(["id"], axis=1)

        return full_df
