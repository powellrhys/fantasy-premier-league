from pages.functions.support_functions import \
    read_csv
from pages.functions.support_functions import \
    summarise_manager_data
from pages.functions.players import \
    create_gameweek_df_for_team
from pages.functions.plots import \
    plot_line_my_team_stats

from dotenv import load_dotenv
import streamlit as st
import os

# Configure page config
st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
) 

load_dotenv()

col1, col2, = st.columns([3,2])

with col1:
    # UI components
    st.title('Team Analysis')

with col2:
    pw = st.text_input('Password', type='password')

if pw != os.getenv('password'):

    st.text('Login to see fantasy team stats')

else:

    # Siderbar position radio component
    position_radio = st.radio(
        label = "Position to Analyse",
        options = ('Goalkeeper', 'Defender', 'Midfielder', 'Forward'), 
        horizontal=True)

    # Sidebar gameweek slider
    gameweek_range = st.slider(
        label='Gameweeks to Analyse',
        min_value = 1,
        max_value = 38,
        value = (1, 38))

    # Collect and filter player data
    players_df = read_csv('data/players.csv')
    player_filter = players_df[players_df['position'] == position_radio]['second_name'].to_list()

    # Configure page tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['GW Points', 'GW Minutes', 'GW Goals', 'GW Assists', 
                                            'GW CS', 'GW Cost'])

    with tab1:
        df, players = create_gameweek_df_for_team('total_points', gameweek_range, player_filter)
        fig = plot_line_my_team_stats(df, players, 'Points')
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        df, players = create_gameweek_df_for_team('minutes', gameweek_range, player_filter)
        fig = plot_line_my_team_stats(df, players, 'Minutes')
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        df, players = create_gameweek_df_for_team('goals_scored', gameweek_range, player_filter)
        fig = plot_line_my_team_stats(df, players, 'Goals Scored')
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        df, players = create_gameweek_df_for_team('assists', gameweek_range, player_filter)
        fig = plot_line_my_team_stats(df, players, 'Assists')
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        df, players = create_gameweek_df_for_team('clean_sheets', gameweek_range, player_filter)
        fig = plot_line_my_team_stats(df, players, 'Clean Sheets')
        st.plotly_chart(fig, use_container_width=True)

    with tab6:
        df, players = create_gameweek_df_for_team('value', gameweek_range, player_filter)
        fig = plot_line_my_team_stats(df, players, 'Cost (M)')
        st.plotly_chart(fig, use_container_width=True)
