# Import dependencies
from backend.functions.data import GameWeek
from unittest.mock import patch

@patch("backend.functions.data.gameweek.FPLApiClient")
def test_get_current_returns_gameweek(mock_client):
    """
    Test normal case where a current gameweek exists.
    """
    # Mock client
    mock_client.return_value.get_json.return_value = {
        "events": [
            {"id": 1, "is_current": False},
            {"id": 2, "is_current": True}
        ]
    }

    result = GameWeek.get_current()
    assert result == 2


@patch("backend.functions.data.gameweek.FPLApiClient")
def test_get_current_outside_season(mock_client):
    """
    Test when there is no current gameweek.
    """
    # Mock client
    mock_client.return_value.get_json.return_value = {
        "events": [
            {"id": 1, "is_current": False},
            {"id": 2, "is_current": False}
        ]
    }

    # Execute get_current and assert values
    result = GameWeek.get_current()
    assert result == "Outside of Season Window"
