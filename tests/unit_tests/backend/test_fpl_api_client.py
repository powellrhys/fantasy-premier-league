# Import dependencies
from backend.functions.data.fpl_api_client import FPLApiClient
from unittest.mock import patch, MagicMock

@patch("backend.functions.data.fpl_api_client.requests.get")
def test_get_json_returns_expected_data(mock_get):
    """
    Test that get_json constructs correct URL, calls requests.get, and returns JSON.
    """
    # Arrange test
    fake_response = {"data": "fake_fpl_data"}

    # Mock response
    mock_response = MagicMock()
    mock_response.json.return_value = fake_response
    mock_get.return_value = mock_response

    # Creaye instance of client
    client = FPLApiClient()
    endpoint = "bootstrap-static"

    # Execute function
    result = client.get_json(endpoint)

    # Assert results
    expected_url = f"{client.BASE_URL}/{endpoint}"
    mock_get.assert_called_once_with(expected_url)
    mock_response.json.assert_called_once()
    assert result == fake_response


@patch("backend.functions.data.fpl_api_client.requests.get")
def test_get_json_handles_different_endpoint(mock_get):
    """
    Ensure get_json works for different endpoints and reuses the same pattern.
    """
    # Mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {"ok": True}
    mock_get.return_value = mock_response

    # Create instance of class
    client = FPLApiClient()
    result = client.get_json("entry/12345/event/1/picks")

    # Assert response
    mock_get.assert_called_once_with("https://fantasy.premierleague.com/api/entry/12345/event/1/picks")
    assert result == {"ok": True}
