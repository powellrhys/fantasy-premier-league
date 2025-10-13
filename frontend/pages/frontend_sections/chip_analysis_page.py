# Import dependencies
from streamlit_components.plot_functions import PlotlyPlotter
import streamlit as st
import pandas as pd

def render_chip_analysis_page(leagues_df: pd.DataFrame) -> None:
    """
    Render the Chip Analysis page in a Streamlit app with interactive visualizations.

    The page allows users to:
    - Select a league from a dropdown menu.
    - View chip usage by players in the selected league.
    - Display a bar chart showing the number of times each player has used
      different FPL chips (Bench Boost, Free Hit, Triple Captain, Wildcard).

    Args:
        leagues_df (pd.DataFrame): A DataFrame containing managerial league data,
                                   including columns like 'player_name', 'league_name',
                                   'league_rank', and chip usage flags ('bench_boost',
                                   'free_hit', 'triple_c', 'wildcard').

    Returns:
        None
    """
    # Collect a unique list of leagues
    list_of_leagues = leagues_df['league_name'].unique()

    # Render league select box
    league_selected = st.selectbox(label='League', options=tuple(list_of_leagues))

    # Filter and transform dataframe
    league_data_df = leagues_df[leagues_df['league_name'] == league_selected] \
        .rename(columns={
            'bench_boost': 'Bench Boost',
            'free_hit': 'Free Hit',
            'triple_c': 'Triple Captain',
            'wildcard': 'Wildcard'})

    # Melt, generate and render results
    df_melted = pd.melt(league_data_df, id_vars=['player_name', 'league_rank'],
                        value_vars=['Bench Boost', 'Free Hit', 'Triple Captain', 'Wildcard'])

    # Render plot within container
    with st.container():
        st.plotly_chart(PlotlyPlotter(
            df=df_melted,
            x='player_name',
            y='value',
            color='variable',
            labels={
                "player_name": "Name",
                "value": "Chips Played",
                "variable": 'Chips'
            }).plot_bar())
