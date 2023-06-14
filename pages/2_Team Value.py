import streamlit as st
import numpy as np

from pages.functions.support_functions import read_csv, position_filter_object
from pages.functions.plots import plot_points_per_team, plot_player_points_bar

st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

player_data_df = read_csv('data/players.csv')

st.markdown("# Team Value Analyis")

# team_position_filter = position_filter_object('team', ['Goalkeeper', 'Defender', 'Midfielder', 'Forward'])

filter_list = np.array(['Goalkeeper', 'Defender', 'Midfielder', 'Forward'])

goal_check = st.sidebar.checkbox('Goalkeeper', value=True)
def_check = st.sidebar.checkbox('Defender', value=True)
mid_check = st.sidebar.checkbox('Midfielder', value=True)
fow_check = st.sidebar.checkbox('Forward', value=True)
 
filter_index= np.array([goal_check, def_check, mid_check, fow_check])
position_filter = filter_list[filter_index]

team_data_df = player_data_df.groupby(by=['team', 'position']).sum()
team_data_df.reset_index(inplace=True)
team_data_df = team_data_df[team_data_df['position'].isin(position_filter)]

points_per_team = plot_points_per_team(team_data_df)
st.plotly_chart(points_per_team, use_container_width=True)
