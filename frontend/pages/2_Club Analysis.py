from pages.functions.ui_components import \
    position_checkbox
from pages.functions.plots import \
    plot_points_per_team, \
    plot_bar_club_stats_bar

from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import requests
import os

# Configure page config
st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

load_dotenv()

# Read current league standings
standings_columns = ['Position', 'Team', 'Pl', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
response = requests.get(f"{os.getenv('api_url')}/players?api_key={os.getenv('password')}")
player_data_df = pd.DataFrame(response.json())

response = requests.get(f"{os.getenv('api_url')}/league-table?api_key={os.getenv('password')}")
premier_league_table = pd.DataFrame(response.json())

# UI components
st.markdown("# Club Analyis")

# Configure page tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Standings', 'Goals Scored', 'Goals Conceded',
                                        'Goal Differene', 'FPL Points'])

with tab1:
    st.table(premier_league_table)

with tab2:
    goals_df = premier_league_table.sort_values(by=['GF'], ascending=False).head(10)
    fig = plot_bar_club_stats_bar(goals_df, 'GF', 'Goals')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    conceded_df = premier_league_table.sort_values(by=['GA'], ascending=False).head(10)
    fig = plot_bar_club_stats_bar(conceded_df, 'GA', 'Goals Conceded')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    difference_df = premier_league_table.sort_values(by=['GD'], ascending=False).head(10)
    fig = plot_bar_club_stats_bar(difference_df, 'GD', 'Goal Difference')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    # Collect position filter input
    position_filter = position_checkbox('club_value_page', vertical=False)

    # Group data by team and position
    team_data_df = player_data_df.groupby(by=['team', 'position']).sum()
    team_data_df.reset_index(inplace=True)

    # Filter data by position
    team_data_df = team_data_df[team_data_df['position'].isin(position_filter)]

    # Generate plot
    points_per_team = plot_points_per_team(team_data_df)
    st.plotly_chart(points_per_team, use_container_width=True)
