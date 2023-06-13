import streamlit as st

from pages.functions.support_functions import read_csv, position_filter_object
from pages.functions.plots import plot_points_per_team

st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

player_data_df = read_csv('data/players.csv')

st.markdown("# Team Value Analyis")

position_filter = position_filter_object()

team_data_df = player_data_df.groupby(by=['team', 'position']).sum()
team_data_df.reset_index(inplace=True)
team_data_df = team_data_df[team_data_df['position'].isin(position_filter)]

points_per_team = plot_points_per_team(team_data_df)
st.plotly_chart(points_per_team, use_container_width=True)
