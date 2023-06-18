from pages.functions.support_functions import summarise_manager_data
from update_data import \
    update_data, \
    update_my_team_data, \
    update_all_player_data

import streamlit as st

# Configure page config
st.set_page_config(
    page_title="Home",
    page_icon=":soccer:",
)

# Collect manager related stats
team_name, region, gameweek_points, overall_points, overall_rank = summarise_manager_data('data/manager_summary.csv')

# UI components
st.title('FPL Dashboard')
st.subheader(f'Team Name: :blue[{team_name}]')
st.subheader(f'Team Region: :blue[{region}]')
st.subheader(f'Latest Gameweek Points: :blue[{gameweek_points}]')
st.subheader(f'Overall Points: :blue[{overall_points}]')
st.subheader(f'Overall Ranking Name: :blue[{overall_rank}]')
