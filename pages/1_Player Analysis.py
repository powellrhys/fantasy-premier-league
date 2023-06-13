import streamlit as st

from pages.functions.support_functions import read_csv
from pages.functions.plots import plot_cost_to_points, plot_minutes_to_points

st.set_page_config(
    page_title="Player Analysis",
    page_icon=":soccer:",
)

player_data_df = read_csv('data/players.csv')

st.markdown("# Player Analyis")

option = st.selectbox(
    'Position',
    ('All', 'Goalkeeper', 'Defender', 'Midfielder', 'Forward'))

if option == 'All':
    filter = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
else:
    filter = [option]

player_data_df = player_data_df[player_data_df['position'].isin(filter)]

cost_to_points = plot_cost_to_points(player_data_df)
st.plotly_chart(cost_to_points, use_container_width=True)

minutes_to_points = plot_minutes_to_points(player_data_df)
st.plotly_chart(minutes_to_points, use_container_width=True)
