# Import dependencies
from frontend.pages.frontend_sections.home_page import render_home_page
from unittest.mock import patch, MagicMock
import pandas as pd
import pytest

@pytest.fixture
def sample_df():
    """Return a small sample dataframe with dream team players."""
    return pd.DataFrame([
        {
            "web_name": "Player1",
            "team": "Arsenal",
            "photo": "player1.jpg",
            "total_points": 100,
            "selected_by_percent": 50.0,
            "now_cost": 100,
            "position": "MID",
            "in_dreamteam": True
        },
        {
            "web_name": "Player2",
            "team": "Liverpool",
            "photo": "player2.jpg",
            "total_points": 90,
            "selected_by_percent": 40.0,
            "now_cost": 95,
            "position": "FWD",
            "in_dreamteam": True
        },
        {
            "web_name": "Player3",
            "team": "Chelsea",
            "photo": "player3.jpg",
            "total_points": 85,
            "selected_by_percent": 30.0,
            "now_cost": 90,
            "position": "DEF",
            "in_dreamteam": False
        }
    ])


@patch("frontend.pages.frontend_sections.home_page.st")
def test_render_home_page(mock_st, sample_df):
    """
    Test that render_home_page correctly calls Streamlit functions and processes dream team players.
    """
    # Mock container and columns
    mock_container = MagicMock()
    mock_columns = [MagicMock() for _ in range(11)]
    mock_st.container.return_value.__enter__.return_value = mock_container
    mock_st.columns.return_value = mock_columns

    # Execute the function
    render_home_page(sample_df)

    # --- Assert page titles ---
    assert mock_st.title.call_count == 2
    mock_st.title.assert_any_call("Fantasy Premier League Dashboard")
    mock_st.title.assert_any_call("Current FPL Dream Team")

    # --- Assert overview paragraph ---
    assert mock_st.write.call_count == 1
    written_text = mock_st.write.call_args[0][0]
    assert "Welcome to FPL Insights" in written_text

    # --- Assert columns for dream team ---
    mock_st.columns.assert_called_once_with(11)

    # --- Assert markdown calls for each dream team player ---
    # Only 2 players are in dream team
    assert sum(1 for call in mock_columns for _ in call.method_calls) == 0
    # Instead, verify markdown was called twice
    assert mock_st.markdown.call_count == 2

    # Check that images are converted to .png URLs
    md_args = [call_args[0][0] for call_args in mock_st.markdown.call_args_list]
    assert all(".png" in md for md in md_args)
    # Check player names appear
    assert all(p["web_name"] in md for p, md in zip(sample_df[sample_df["in_dreamteam"]].to_dict("records"), md_args))
