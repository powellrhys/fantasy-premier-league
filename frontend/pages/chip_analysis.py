# Import python and project dependencies
from streamlit_components.ui_components import configure_page_config
from streamlit_components.plot_functions import PlotlyPlotter
from shared.functions import BlobStorage, Variables
import streamlit as st
import pandas as pd

# Set page config
configure_page_config(repository_name='fantasy-premier-league',
                      page_icon=":soccer:")

# Ensure user is authenticated to use application
if not st.user.is_logged_in:
    st.login('auth0')

st.title("Chip Analysis")

# If user logged in, render streamlit content
if st.user.is_logged_in and st.user["name"] in Variables().privileged_users:

    leagues_df = BlobStorage().read_csv_from_blob(file_name="leagues_data.csv")

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

else:
    st.error(
        f"""
        **{st.user["name"]}** does not have access to this page!!

        The following page contains information specific to privileged users of the project
        and therefore cannot be viewed
        """
    )
