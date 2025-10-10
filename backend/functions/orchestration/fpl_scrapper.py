# Import dependencies
from shared.functions import BlobStorage, Variables
from ..data import GameWeek, PlayerData, League
from ..logging import configure_logging
import pandas as pd

class FPLScrapper(BlobStorage):
    """
    A class to run the Fantasy Premier League data scraping workflow and store results in blob storage.
    """

    def __init__(self) -> None:
        """
        Initialize the FPLScrapper with logging and variable configuration.
        """
        self.logger = configure_logging()
        self.vars = Variables()

    def run(self) -> None:
        """
        Execute the data scraping workflow:
        1. Determine the current game week.
        2. Collect player data.
        3. Collect league standings and chip usage data for each league.
        4. Store the collected data in blob storage.
        """
        # Log start of process
        self.logger.info("Running Workflow Scrapping flow \n")

        # Collect current game week
        self.logger.info('Determining current Game Week...')
        gw = GameWeek().get_current()
        self.logger.info(f'Current Game Week: {gw} \n')

        # Collect player data
        self.logger.info('Collecting player data...')
        player_df = PlayerData().get_player_dataframe()
        self.logger.info(f'Data collected for {len(player_df)} players \n')

        # Export data
        self.logger.info('Writing player data to blob storage...')
        BlobStorage().upload_dataframe(df=player_df, file_name='player_data.csv')
        self.logger.info('Player data written to blob storage \n')

        # Iterate through each league and collect data
        all_league_df = pd.DataFrame()
        for ind, league_id in enumerate(self.vars.league_ids, start=1):

            # Collect league data
            self.logger.info(f"{ind}/{len(self.vars.league_ids)} - Collecting managerial "
                             f"league data for league id: {league_id}...")
            league_df = League(league_id=league_id).collect_league_data()
            all_league_df = pd.concat([all_league_df, league_df], ignore_index=True)

        # Export league data
        self.logger.info('Writing managerial league data to blob storage...')
        BlobStorage().upload_dataframe(df=all_league_df, file_name='leagues_data.csv')
        self.logger.info('Managerial league data written to blob storage \n')
