# Import dependencies
from backend.functions.data.manager import Manager
from unittest.mock import patch

@patch("backend.functions.data.manager.FPLApiClient")
def test_get_chip_flags_with_used_chips(mock_fpl_api_client):
    """
    Test get_chip_flags returns correct binary flags when chips are used.
    """
    # Arrange test
    mock_instance = mock_fpl_api_client.return_value
    mock_instance.get_json.return_value = {
        "chips": [
            {"name": "bboost"},
            {"name": "3xc"},
            {"name": "wildcard"},
        ]
    }

    # Create instance of manager
    manager = Manager(manager_id=123)

    # Execute function
    result = manager.get_chip_flags()

    # Assert response
    mock_instance.get_json.assert_called_once_with("entry/123/history/")

    # Ensure expected results matches result
    expected_result = {
        "entry": 123,
        "bench_boost": 1,
        "free_hit": 0,
        "triple_c": 1,
        "wildcard": 1,
    }

    assert result == expected_result

@patch("backend.functions.data.manager.FPLApiClient")
def test_get_chip_flags_with_no_chips(mock_fpl_api_client):
    """
    Test get_chip_flags returns all zero flags when no chips were used.
    """
    # Mock instance of class
    mock_instance = mock_fpl_api_client.return_value
    mock_instance.get_json.return_value = {"chips": []}

    # Create manager instance
    manager = Manager(manager_id=999)
    result = manager.get_chip_flags()

    # Ensure result matches expected result
    expected_result = {
        "entry": 999,
        "bench_boost": 0,
        "free_hit": 0,
        "triple_c": 0,
        "wildcard": 0,
    }

    assert result == expected_result


@patch("backend.functions.data.manager.FPLApiClient")
def test_get_chip_flags_handles_missing_chips_key(mock_fpl_api_client):
    """
    Ensure get_chip_flags handles missing 'chips' key gracefully.
    """
    # Mock instance
    mock_instance = mock_fpl_api_client.return_value
    mock_instance.get_json.return_value = {}

    # Create instance of Manager Class
    manager = Manager(manager_id=42)
    result = manager.get_chip_flags()

    # It should still return the manager ID and all zeros for flags
    assert result["entry"] == 42
    assert all(value == 0 for key, value in result.items() if key != "entry")
