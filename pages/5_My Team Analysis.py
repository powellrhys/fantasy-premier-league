import streamlit as st
import pandas as pd
import os

from pages.functions.support_functions import \
    read_csv
from pages.functions.support_functions import summarise_manager_data
from pages.functions.plots import plot_line_my_team_stats
from pages.functions.players import create_gameweek_df_for_team

st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
) 
team_name, _, _, _, _ = summarise_manager_data('data/manager_summary.csv')  

st.title(f'{team_name} Analysis')

gameweek_range = st.sidebar.slider(
    'Gameweeks to Analyse',
    1, 38, (1, 38))

position_radio = st.sidebar.radio(
    "Position to Analyse",
    ('Goalkeeper', 'Defender', 'Midfielder', 'Forward'))

players_df = read_csv('data/players.csv')
player_filter = players_df[players_df['position'] == position_radio]['second_name'].to_list()

tab1, tab2 = st.tabs(['GW Points', 'GW Minutes'])

with tab1:
    df, players = create_gameweek_df_for_team('total_points', gameweek_range, player_filter)
    fig = plot_line_my_team_stats(df, players, 'Points')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    df, players = create_gameweek_df_for_team('minutes', gameweek_range, player_filter)
    fig = plot_line_my_team_stats(df, players, 'Minutes')
    st.plotly_chart(fig, use_container_width=True)

