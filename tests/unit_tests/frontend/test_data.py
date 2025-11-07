# Import dependencies
from frontend.functions.data import collect_player_data, collect_managerial_league_data, wake_up_database
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

@patch("frontend.functions.data.time.sleep", return_value=None)  # avoid real sleeping
@patch("frontend.functions.data.st")
@patch("frontend.functions.data.pd.read_sql")
@patch("frontend.functions.data.DatabaseConnector")
def test_wake_up_database_success(mock_db_connector, mock_read_sql, mock_st, mock_sleep):
    """
    Test when the SQL Server is reachable on the first attempt.
    """
    # Mock engine and connector
    mock_engine = MagicMock()
    mock_db_connector.return_value.get_engine.return_value = mock_engine

    # read_sql succeeds immediately
    mock_read_sql.return_value = None

    # Call the function
    result = wake_up_database()

    # Assertions
    assert result is True
    mock_read_sql.assert_called_once_with("SELECT 1", mock_engine)
    mock_st.spinner.assert_called_once()
    mock_st.error.assert_not_called()


@patch("frontend.functions.data.time.sleep", return_value=None)
@patch("frontend.functions.data.st")
@patch("frontend.functions.data.pd.read_sql", side_effect=Exception("DB down"))
@patch("frontend.functions.data.DatabaseConnector")
def test_wake_up_database_failure(mock_db_connector, mock_read_sql, mock_st, mock_sleep):
    """
    Test when all retries fail to connect to SQL Server.
    """
    mock_engine = MagicMock()
    mock_db_connector.return_value.get_engine.return_value = mock_engine

    # Mock Streamlit placeholder
    mock_placeholder = MagicMock()
    mock_st.empty.return_value = mock_placeholder

    result = wake_up_database()

    # Assertions
    assert result is False
    assert mock_read_sql.call_count == 5  # retried 5 times
    mock_placeholder.info.assert_called()  # should display retry info
    mock_st.error.assert_called_once_with("SQL Server Offline - Try again later")
