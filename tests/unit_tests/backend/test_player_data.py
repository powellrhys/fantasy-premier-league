# Import dependencies
from backend.functions.data_schemas import player_data_columns

def test_player_data_columns_structure():
    """Verify player_data_columns is a list of strings."""
    assert isinstance(player_data_columns, list), "player_data_columns should be a list"
    assert all(isinstance(col, str) for col in player_data_columns), "all column names must be strings"


def test_player_data_columns_expected_fields():
    """Ensure all expected player data fields are present and in correct order."""
    expected_columns = [
        'id',
        'web_name',
        'team',
        'element_type',
        'selected_by_percent',
        'now_cost',
        'minutes',
        'transfers_in',
        'value_season',
        'total_points',
        'goals_scored',
        'assists',
        'clean_sheets',
        'goals_conceded',
        'own_goals',
        'penalties_saved',
        'penalties_missed',
        'yellow_cards',
        'red_cards',
        'saves',
        'starts',
        'photo',
        'in_dreamteam',
        'defensive_contribution_per_90'
    ]

    # Assert same length and identical ordered content
    assert player_data_columns == expected_columns, "player_data_columns should match the expected list exactly"


def test_player_data_columns_no_duplicates():
    """Verify no duplicate field names exist."""
    assert len(player_data_columns) == len(set(player_data_columns)), \
        "Duplicate column names found in player_data_columns"
