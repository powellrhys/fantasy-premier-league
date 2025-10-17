# Import dependencies
from frontend.functions.data import collect_player_data, collect_managerial_league_data
from unittest.mock import patch, MagicMock
import pandas as pd
import pytest


@pytest.fixture
def mock_dataframe():
    """
    Fixture providing a simple mock DataFrame for testing.

    Returns:
        pd.DataFrame: A small DataFrame with two rows and columns 'id' and 'name'.
    """
    return pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})

@patch("frontend.functions.data.PlayerRepository")
@patch("frontend.functions.data.DatabaseConnector")
def test_collect_player_data(mock_db_connector, mock_player_repo, mock_dataframe):
    """
    Test that collect_player_data() returns the expected DataFrame and correctly
    initializes both the DatabaseConnector and PlayerRepository mocks.

    The database connection and data retrieval are fully mocked to prevent
    any real SQL interaction.
    """
    # Arrange: create a mock PlayerRepository instance and configure it to return mock data
    mock_instance = MagicMock()
    mock_instance.read_dataframe.return_value = mock_dataframe
    mock_player_repo.return_value = mock_instance

    # Act: call the function under test
    result = collect_player_data()

    # Assert: verify that all dependencies were called as expected
    mock_db_connector.assert_called_once_with(source="Frontend")
    mock_player_repo.assert_called_once_with(db_connector=mock_db_connector.return_value)
    mock_instance.read_dataframe.assert_called_once()

    # Assert: check that the returned DataFrame matches our mock
    pd.testing.assert_frame_equal(result, mock_dataframe)

@patch("frontend.functions.data.LeagueRepository")
@patch("frontend.functions.data.DatabaseConnector")
def test_collect_managerial_league_data(mock_db_connector, mock_league_repo, mock_dataframe):
    """
    Test that collect_managerial_league_data() returns the expected DataFrame and
    properly uses DatabaseConnector and LeagueRepository mocks.

    This ensures that the function logic and data flow are correct without
    requiring a real database connection.
    """
    # Arrange: create a mock LeagueRepository instance and configure it to return mock data
    mock_instance = MagicMock()
    mock_instance.read_dataframe.return_value = mock_dataframe
    mock_league_repo.return_value = mock_instance

    # Act: call the function under test
    result = collect_managerial_league_data()

    # Assert: verify that dependencies were called correctly
    mock_db_connector.assert_called_once_with(source="Frontend")
    mock_league_repo.assert_called_once_with(db_connector=mock_db_connector.return_value)
    mock_instance.read_dataframe.assert_called_once()

    # Assert: check that the returned DataFrame matches our mock
    pd.testing.assert_frame_equal(result, mock_dataframe)
