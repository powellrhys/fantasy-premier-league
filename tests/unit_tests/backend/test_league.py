# Import dependencies
from unittest.mock import patch, MagicMock
from backend.functions.data import League
import pandas as pd
import pytest

@pytest.fixture
def mock_league_data():
    """Mock API response for a sample league."""
    return {
        "league": {"name": "Mock League"},
        "standings": {
            "results": [
                {"entry": 1, "player_name": "Alice", "rank": 1, "id": 101},
                {"entry": 2, "player_name": "Bob", "rank": 2, "id": 102},
            ]
        },
    }


@pytest.fixture
def mock_chip_data():
    """Mock chip flags returned by Manager.get_chip_flags()."""
    return [
        {"entry": 1, "used_wildcard": True, "used_triple_captain": False},
        {"entry": 2, "used_wildcard": False, "used_triple_captain": True},
    ]


@patch("backend.functions.data.FPLApiClient")
@patch("backend.functions.data.Manager")
def test_collect_league_data_returns_dataframe(mock_manager_cls, mock_client_cls, mock_league_data, mock_chip_data):
    """
    Test that collect_league_data returns a correctly merged DataFrame.
    """
    # Mock FPLApiClient.get_json
    mock_client_instance = MagicMock()
    mock_client_instance.get_json.return_value = mock_league_data
    mock_client_cls.return_value = mock_client_instance

    # Mock Manager.get_chip_flags for each entry
    mock_manager_instance = MagicMock()
    mock_manager_instance.get_chip_flags.side_effect = mock_chip_data
    mock_manager_cls.return_value = mock_manager_instance

    # Create League instance
    league = League(league_id="12345")

    # Call method
    df = league.collect_league_data()

    # Verify DataFrame structure
    assert isinstance(df, pd.DataFrame)
    assert "id" not in df.columns

@patch("backend.functions.data.FPLApiClient")
def test_collect_league_data_api_error(mock_client_cls):
    """
    Test that an exception from the API is raised or handled gracefully.
    """
    # Mock test
    mock_client_instance = MagicMock()
    mock_client_instance.get_json.side_effect = Exception("API Error")
    mock_client_cls.return_value = mock_client_instance

    # Execute test
    league = League("error123")
    with pytest.raises(Exception):
        league.collect_league_data()
