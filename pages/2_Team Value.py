import streamlit as st

from pages.functions.support_functions import read_csv, position_filter_object
from pages.functions.plots import plot_points_per_team, plot_player_points_bar

st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

player_data_df = read_csv('data/players.csv')

st.markdown("# Team Value Analyis")

team_position_filter = position_filter_object('team', ['Goalkeeper', 'Defender', 'Midfielder', 'Forward'])

team_data_df = player_data_df.groupby(by=['team', 'position']).sum()
team_data_df.reset_index(inplace=True)
team_data_df = team_data_df[team_data_df['position'].isin(team_position_filter)]

points_per_team = plot_points_per_team(team_data_df)
st.plotly_chart(points_per_team, use_container_width=True)

player_position_filter = st.selectbox(
    'Position',
    ('Goalkeeper', 'Defender', 'Midfielder', 'Forward'))

player_data_df['points_per_cost'] = player_data_df['total_points'] / player_data_df['now_cost']
player_data_df_filtered = player_data_df[player_data_df['position'] == player_position_filter]

top15_player_data_df_filtered = player_data_df_filtered.sort_values(by=['total_points'], ascending=False).head(15)
top15_player_data_df_filtered_normalised = player_data_df_filtered.sort_values(by=['points_per_cost'], ascending=False).head(15)

points_per_position = plot_player_points_bar(top15_player_data_df_filtered, 'total_points', 'Total Points')
st.plotly_chart(points_per_position, use_container_width=True)

points_per_position_normalised = plot_player_points_bar(top15_player_data_df_filtered_normalised, 'points_per_cost', 'Points per Unit Cost')
st.plotly_chart(points_per_position_normalised, use_container_width=True)