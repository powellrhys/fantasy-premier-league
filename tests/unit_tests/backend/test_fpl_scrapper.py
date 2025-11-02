# Import dependencies
from backend.functions.orchestration import FPLScrapper
from unittest.mock import patch, MagicMock
import pandas as pd
import unittest


class TestFPLScrapper(unittest.TestCase):
    """
    Unit tests for FPLScrapper class — one per method.
    """

    @patch("backend.functions.orchestration.fpl_scrapper.LeagueRepository")
    @patch("backend.functions.orchestration.fpl_scrapper.PlayerRepository")
    @patch("backend.functions.orchestration.fpl_scrapper.DatabaseConnector")
    @patch("backend.functions.orchestration.fpl_scrapper.configure_logging")
    @patch("backend.functions.orchestration.fpl_scrapper.Variables")
    def test_init_creates_repositories(self, mock_vars, mock_logger, mock_db, mock_player_repo, mock_league_repo):
        """
        Test that init sets up repositories and logging correctly.
        """
        # Define class
        scrapper = FPLScrapper()

        # Assert executions
        mock_logger.assert_called_once()
        mock_db.assert_called_once()
        mock_player_repo.assert_called_once()
        mock_league_repo.assert_called_once()

        # Ensure values are not null
        self.assertIsNotNone(scrapper.logger)
        self.assertIsNotNone(scrapper.player_repository)
        self.assertIsNotNone(scrapper.league_repository)

    @patch("backend.functions.orchestration.fpl_scrapper.FPLScrapper._collect_and_store_league_data")
    @patch("backend.functions.orchestration.fpl_scrapper.FPLScrapper._collect_and_store_player_data")
    @patch("backend.functions.orchestration.fpl_scrapper.FPLScrapper._get_current_game_week")
    @patch("backend.functions.orchestration.fpl_scrapper.configure_logging")
    @patch("backend.functions.orchestration.fpl_scrapper.Variables")
    @patch("backend.functions.orchestration.fpl_scrapper.DatabaseConnector")
    @patch("backend.functions.orchestration.fpl_scrapper.PlayerRepository")
    @patch("backend.functions.orchestration.fpl_scrapper.LeagueRepository")
    def test_run_executes_workflow(
        self, mock_league_repo, mock_player_repo, mock_db, mock_vars,
        mock_logger, mock_gw, mock_collect_players, mock_collect_leagues
    ):
        """
        Test that run executes full workflow sequence.
        """
        # Create mocked values
        mock_logger.return_value.info = MagicMock()
        mock_gw.return_value = "GW10"

        # Call class
        scrapper = FPLScrapper()
        scrapper.run()

        # Assert mocked results
        mock_logger.return_value.info.assert_any_call("Running Fantasy Premier League Scrapping flow \n")
        mock_gw.assert_called_once()
        mock_collect_players.assert_called_once()
        mock_collect_leagues.assert_called_once()
        mock_logger.return_value.info.assert_any_call("Fantasy Premier League Scrapping flow completed.\n")

    @patch("backend.functions.orchestration.fpl_scrapper.PlayerData")
    @patch("backend.functions.orchestration.fpl_scrapper.configure_logging")
    @patch("backend.functions.orchestration.fpl_scrapper.Variables")
    @patch("backend.functions.orchestration.fpl_scrapper.DatabaseConnector")
    @patch("backend.functions.orchestration.fpl_scrapper.PlayerRepository")
    @patch("backend.functions.orchestration.fpl_scrapper.LeagueRepository")
    def test_collect_and_store_player_data_saves_to_db(
        self, mock_league_repo, mock_player_repo, mock_db, mock_vars, mock_logger, mock_player_data
    ):
        """
        Test that _collect_and_store_player_data collects and writes player data.
        """
        # Mock dataframe and define class
        mock_player_data.return_value.get_player_dataframe.return_value = pd.DataFrame({"name": ["Haaland", "Salah"]})
        scrapper = FPLScrapper()

        # Execute collect store player data
        scrapper._collect_and_store_player_data()

        # Assert response
        mock_player_data.return_value.get_player_dataframe.assert_called_once()
        scrapper.player_repository.append_new_data_to_database.assert_called_once()

    @patch("backend.functions.orchestration.fpl_scrapper.League")
    @patch("backend.functions.orchestration.fpl_scrapper.configure_logging")
    @patch("backend.functions.orchestration.fpl_scrapper.Variables")
    @patch("backend.functions.orchestration.fpl_scrapper.DatabaseConnector")
    @patch("backend.functions.orchestration.fpl_scrapper.PlayerRepository")
    @patch("backend.functions.orchestration.fpl_scrapper.LeagueRepository")
    def test_collect_and_store_league_data_combines_and_saves(
        self, mock_league_repo, mock_player_repo, mock_db, mock_vars, mock_logger, mock_league_cls
    ):
        """
        Test that _collect_and_store_league_data merges and writes league data.
        """
        # Mock inputs
        mock_vars.return_value.league_ids = ["111", "222"]
        mock_league_cls.return_value.collect_league_data.side_effect = [
            pd.DataFrame({"entry": [1], "points": [100]}),
            pd.DataFrame({"entry": [2], "points": [90]}),
        ]

        # Define class and call store league data
        scrapper = FPLScrapper()
        scrapper._collect_and_store_league_data()

        # Should have concatenated 2 leagues into a combined df and saved
        self.assertTrue(scrapper.league_repository.append_new_data_to_database.called)
        calls = mock_league_cls.return_value.collect_league_data.call_count
        self.assertEqual(calls, 2)
