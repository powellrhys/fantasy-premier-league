# Import dependencies
from streamlit_components.plot_functions import PlotlyPlotter
import streamlit as st
import pandas as pd

def render_chip_analysis_page(leagues_df: pd.DataFrame) -> None:
    """
    """
    list_of_leagues = leagues_df['league_name'].unique()
    league_selected = st.selectbox(
        label='League',
        options=tuple(list_of_leagues))

    league_data_df = leagues_df[leagues_df['league_name'] == league_selected].rename(columns={
        'bench_boost': 'Bench Boost',
        'free_hit': 'Free Hit',
        'triple_c': 'Triple Captain',
        'wildcard': 'Wildcard'})

    # Melt, generate and render results
    df_melted = pd.melt(league_data_df, id_vars=['player_name', 'league_rank'],
                        value_vars=['Bench Boost', 'Free Hit', 'Triple Captain', 'Wildcard'])

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
