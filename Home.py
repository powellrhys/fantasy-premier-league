from pages.functions.support_functions import summarise_manager_data
from update_data import \
    update_data, \
    update_my_team_data, \
    update_all_player_data

import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":soccer:",
)

team_name, region, gameweek_points, overall_points, overall_rank = summarise_manager_data('data/manager_summary.csv')

st.title('FPL Dashboard')

st.subheader(f'Team Name: :blue[{team_name}]')
st.subheader(f'Team Region: :blue[{region}]')
st.subheader(f'Latest Gameweek Points: :blue[{gameweek_points}]')
st.subheader(f'Overall Points: :blue[{overall_points}]')
st.subheader(f'Overall Ranking Name: :blue[{overall_rank}]')


update_data_button = st.sidebar.button('Update General Data')

if update_data_button:
    with st.spinner('Collecting Data...'):
        update_data()

update_my_team_data_button = st.sidebar.button(f'Update {team_name} Data')

if update_my_team_data_button:
    with st.spinner('Collecting Team Data...'):
        update_my_team_data()    

update_all_player_data_button = st.sidebar.button(f'Update All Player Data')

if update_all_player_data_button:
    with st.spinner('Collecting All Player Data...'):
        update_all_player_data()  