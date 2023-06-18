from pages.functions.support_functions import \
    read_csv
from pages.functions.support_functions import \
    summarise_manager_data
from pages.functions.players import \
    create_gameweek_df_for_team
from pages.functions.plots import \
    plot_line_my_team_stats

import streamlit as st

# Configure page config
st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
) 

# Collect user team name
team_name, _, _, _, _ = summarise_manager_data('data/manager_summary.csv')  

# UI components
st.title(f'{team_name} Analysis')

# Sidebar gameweek slider
gameweek_range = st.sidebar.slider(
    'Gameweeks to Analyse',
    1, 38, (1, 38))

# Siderbar position radio component
position_radio = st.sidebar.radio(
    "Position to Analyse",
    ('Goalkeeper', 'Defender', 'Midfielder', 'Forward'))

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
