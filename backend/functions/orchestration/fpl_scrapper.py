# Import dependencies
from shared.functions.sql import DatabaseConnector, PlayerRepository, LeagueRepository
from ..data import GameWeek, PlayerData, League, GameWeekUpdatingException
from shared.functions import Variables
from ..logging import configure_logging
from typing import Optional
import pandas as pd

class FPLScrapper():
    """
    A class to run the Fantasy Premier League data scraping workflow and store results in a database.
    """

    def __init__(self) -> None:
        """
        Initialize the FPLScrapper with logging and variable configuration.
        """
        self.logger = configure_logging()
        self.vars = Variables()
        db_connector = DatabaseConnector()
        self.player_repository = PlayerRepository(db_connector=db_connector)
        self.league_repository = LeagueRepository(db_connector=db_connector)

    def run(self) -> None:
        """
        Execute the data scraping workflow:
        1. Determine the current game week.
        2. Collect player data.
        3. Collect league standings and chip usage data for each league.
        4. Store the collected data in blob storage.
        """
        # Log start of process
        self.logger.info("Running Fantasy Premier League Scrapping flow \n")

        # Collect current game week
        gw = self._get_current_game_week()

        # Check if game week data currently being updated within api
        if isinstance(gw, str) and "being updated" in gw:
            self.logger.error("Game week data currently being updated. No data currently available")
            raise GameWeekUpdatingException("FPL API is currently updating. Try again later.")

        # Collect and export player data
        self._collect_and_store_player_data()

        # Collect and export league data
        self._collect_and_store_league_data()

        self.logger.info("Fantasy Premier League Scrapping flow completed.\n")

    def _get_current_game_week(self) -> Optional[str]:
        """
        Collect current game week information.

        Returns:
            The current game week as a string, or None if it cannot be determined.
        """
        # Try and collect current game week
        self.logger.info('Determining current Game Week...')
        try:
            gw = GameWeek().get_current()

            if not isinstance(gw, str) and "being updated" not in gw:
                self.logger.info(f'Current Game Week: {gw} \n')
            return gw

        except Exception as e:
            self.logger.warning(f"Failed to determine current Game Week. Error: {e}")
            self.logger.warning("Continuing workflow without Game Week info.\n")
            return None

    def _collect_and_store_player_data(self) -> None:
        """
        Collect player data and write it to the database.

        Returns: None
        """
        # Collect player data from fantasy premier league api
        self.logger.info('Collecting player data...')
        player_df = None
        try:
            player_df = PlayerData().get_player_dataframe()
            self.logger.info(f'Data collected for {len(player_df)} players \n')
        except Exception as e:
            self.logger.error(f"Failed to collect player data: {e}", exc_info=True)
            self.logger.warning("Skipping player data export and continuing workflow.\n")

        # Export player data to SQL only if data collection was successful
        try:
            self.logger.info("Writing player data to database...")
            self.player_repository.append_new_data_to_database(df=player_df)
            self.logger.info("Player data written to SQL \n")
        except Exception as e:
            self.logger.error(f"Failed to write player data to database: {e}", exc_info=True)
            self.logger.warning("Continuing workflow despite database write failure.\n")

    def _collect_and_store_league_data(self) -> None:
        """
        Collect league data for each configured league and write it to the database.

        Returns: None
        """
        # Iterate through each league and collect data
        all_league_df = pd.DataFrame()
        for ind, league_id in enumerate(self.vars.league_ids, start=1):
            self.logger.info(
                f"{ind}/{len(self.vars.league_ids)} - Collecting managerial league data for league id: {league_id}..."
            )

            # Try and collect league specific data
            try:
                league_df = League(league_id=league_id).collect_league_data()
                if league_df is None or league_df.empty:
                    self.logger.warning(f"No data returned for league id {league_id}. Skipping.")
                    continue

                # Concatenating new data to complete dataframe
                all_league_df = pd.concat([all_league_df, league_df], ignore_index=True)

            except Exception as e:
                self.logger.error(f"Failed to collect data for league id {league_id}: {e}", exc_info=True)
                self.logger.warning(f"Skipping league id {league_id} and continuing...\n")

        # If league dataframe not empty, try and export data to SQL
        if all_league_df.empty:
            self.logger.error("No league data collected for any league. Skipping database export.\n")
            return

        try:
            self.logger.info("Writing managerial league data to database...")
            self.league_repository.append_new_data_to_database(df=all_league_df)
            self.logger.info("Managerial League data written to SQL.\n")
        except Exception as e:
            self.logger.error(f"Failed to write league data to database: {e}", exc_info=True)
            self.logger.warning("Continuing workflow despite database write failure.\n")
