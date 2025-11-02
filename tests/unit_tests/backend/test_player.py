# Import dependencies
from backend.functions.data import PlayerData
from unittest.mock import patch
import pandas as pd

@patch("backend.functions.data.player.player_data_columns", ["id", "element_type", "team", "value_season", "now_cost"])
@patch("backend.functions.data.player.FPLApiClient")
def test_get_player_dataframe_normal(mock_client):
    """
    Test normal data retrieval and processing.
    """
    # Mock API response structure
    mock_client.return_value.get_json.return_value = {
        "elements": [
            {"id": 1, "element_type": 2, "team": 1, "value_season": "5.0", "now_cost": 55},
        ],
        "element_types": [{"id": 2, "singular_name": "Midfielder"}],
        "teams": [{"id": 1, "name": "Arsenal"}],
    }

    # Create dataframe
    df = PlayerData().get_player_dataframe()

    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["element_type", "team", "value_season", "now_cost", "position"]
    assert df.loc[1, "position"] == "Midfielder"
    assert df.loc[1, "team"] == "Arsenal"
    assert df.loc[1, "value_season"] == "5.0"
    assert df.loc[1, "now_cost"] == 5.5


@patch("backend.functions.data.player.player_data_columns", ["id", "element_type", "team", "value_season", "now_cost"])
@patch("backend.functions.data.player.FPLApiClient")
def test_get_player_dataframe_handles_multiple_rows(mock_client):
    """
    Test multiple players and ensures index and mapping correctness.
    """
    # Mock client
    mock_client.return_value.get_json.return_value = {
        "elements": [
            {"id": 1, "element_type": 1, "team": 1, "value_season": "10.5", "now_cost": 100},
            {"id": 2, "element_type": 2, "team": 2, "value_season": "7.3", "now_cost": 72},
        ],
        "element_types": [
            {"id": 1, "singular_name": "Goalkeeper"},
            {"id": 2, "singular_name": "Defender"},
        ],
        "teams": [
            {"id": 1, "name": "Liverpool"},
            {"id": 2, "name": "Chelsea"},
        ],
    }

    # Create dataframe
    df = PlayerData().get_player_dataframe()

    # Assertions
    assert len(df) == 2
    assert df.loc[1, "position"] == "Goalkeeper"
    assert df.loc[2, "position"] == "Defender"
    assert df.loc[1, "team"] == "Liverpool"
    assert df.loc[2, "team"] == "Chelsea"
    assert df.loc[1, "now_cost"] == 10.0
    assert df.index.name == "id"
