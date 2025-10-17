# Import dependencies
from shared.functions.sql.players_repository import PlayerRepository
from unittest.mock import MagicMock, patch
import pandas as pd
import pytest

@pytest.fixture
def sample_df():
    """
    Sample DataFrame to use in append_new_data_to_database tests.
    """
    return pd.DataFrame([
        {"player_name": "Alice", "total_points": 100},
        {"player_name": "Bob", "total_points": 90},
    ])


@patch("shared.functions.sql.players_repository.pd.read_sql")
def test_read_dataframe(mock_read_sql):
    """
    Test that read_dataframe calls pd.read_sql with correct query and engine.
    """
    # Arrange test
    mock_engine = MagicMock()
    mock_read_sql.return_value = "fake_dataframe"
    repo = PlayerRepository(db_connector=MagicMock(get_engine=lambda: mock_engine))

    # Execute read_dataframe function
    result = repo.read_dataframe()

    # Assert the select statement gets called once
    mock_read_sql.assert_called_once_with("SELECT * FROM player_overview", mock_engine)
    assert result == "fake_dataframe"


@patch("shared.functions.sql.players_repository.PlayerOverview")
def test_append_new_data_to_database(mock_player_overview_class, sample_df):
    """
    Test append_new_data_to_database calls session methods correctly.
    """
    # Arrange test
    mock_session = MagicMock()
    mock_db_connector = MagicMock()
    mock_db_connector.get_engine.return_value = MagicMock()
    mock_db_connector.Session.return_value = mock_session

    # Create instance of repo
    repo = PlayerRepository(db_connector=mock_db_connector)

    # Mock PlayerOverview instances
    mock_player_overview_class.side_effect = lambda **kwargs: f"player_obj_{kwargs['player_name']}"

    # Act
    repo.append_new_data_to_database(sample_df)

    # Assert bulk_save_objects called with transformed objects
    mock_session.bulk_save_objects.assert_called_once()
    bulk_args = mock_session.bulk_save_objects.call_args[0][0]
    assert all(obj.startswith("player_obj_") for obj in bulk_args)

    # Assert commit called twice (insert + delete)
    assert mock_session.commit.call_count == 2

    # Assert delete executed with current timestamp
    delete_call = mock_session.execute.call_args[0][0].text \
        if hasattr(mock_session.execute.call_args[0][0], 'text')else str(mock_session.execute.call_args[0][0])

    assert "DELETE FROM player_overview" in delete_call

    # Assert session closed
    mock_session.close.assert_called_once()
