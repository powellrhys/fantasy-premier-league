from frontend.pages.frontend_sections.chip_analysis_page import render_chip_analysis_page
from unittest.mock import patch, MagicMock
import pandas as pd
import pytest


@pytest.fixture
def sample_leagues_df():
    """Return a sample leagues DataFrame for testing."""
    return pd.DataFrame([
        {"player_name": "Alice", "league_name": "League A", "league_rank": 1,
         "bench_boost": True, "free_hit": False, "triple_c": True, "wildcard": False},
        {"player_name": "Bob", "league_name": "League A", "league_rank": 2,
         "bench_boost": False, "free_hit": True, "triple_c": False, "wildcard": True},
        {"player_name": "Charlie", "league_name": "League B", "league_rank": 1,
         "bench_boost": True, "free_hit": True, "triple_c": False, "wildcard": True},
    ])


@patch("frontend.pages.frontend_sections.chip_analysis_page.PlotlyPlotter")
@patch("frontend.pages.frontend_sections.chip_analysis_page.st")
def test_render_chip_analysis_page(mock_st, mock_plotly_plotter, sample_leagues_df):
    """
    Test render_chip_analysis_page() with mocked Streamlit and PlotlyPlotter.
    """

    # Arrange: mock selectbox to return 'League A'
    mock_st.selectbox.return_value = "League A"

    # Mock PlotlyPlotter instance and its plot_bar method
    mock_plot_instance = MagicMock()
    mock_plot_instance.plot_bar.return_value = "fake_plot_object"
    mock_plotly_plotter.return_value = mock_plot_instance

    # Act: call the function
    render_chip_analysis_page(sample_leagues_df)

    # --- Assert Streamlit selectbox ---
    expected_leagues = tuple(sample_leagues_df['league_name'].unique())
    mock_st.selectbox.assert_called_once_with(label='League', options=expected_leagues)

    # --- Assert PlotlyPlotter instantiation ---
    args, kwargs = mock_plotly_plotter.call_args
    df_arg = kwargs.get('df') if 'df' in kwargs else args[0]

    # df_arg should contain columns: player_name, league_rank, variable, value
    expected_cols = ['player_name', 'league_rank', 'variable', 'value']
    assert all(col in df_arg.columns for col in expected_cols), \
        f"Missing columns in df passed to PlotlyPlotter: {df_arg.columns}"

    # Only League A players should be present
    assert set(df_arg['player_name'].unique()) == {"Alice", "Bob"}

    # The 'value' column should only contain integers 0 or 1
    assert df_arg['value'].isin([0, 1]).all()

    # --- Assert plot_bar() called and result passed to st.plotly_chart ---
    mock_plot_instance.plot_bar.assert_called_once()
    mock_st.plotly_chart.assert_called_once_with("fake_plot_object")
