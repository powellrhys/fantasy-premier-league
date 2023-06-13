import streamlit as st

from pages.functions.support_functions import read_csv, position_filter_object
from pages.functions.plots import plot_cost_to_points, plot_minutes_to_points, plot_popularity_to_points

st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

player_data_df = read_csv('data/players.csv')

st.markdown("# Player Value Analyis")

position_filter = position_filter_object()

budget_filter = st.slider(label='Budget',
                          min_value=0.0, 
                          max_value=14.0, 
                          value=14.0, 
                          step=0.1)

player_data_df = player_data_df[player_data_df['position'].isin(position_filter)]
player_data_df = player_data_df[player_data_df['now_cost'] <= budget_filter]

cost_to_points = plot_cost_to_points(player_data_df)
st.plotly_chart(cost_to_points, use_container_width=True)

minutes_to_points = plot_minutes_to_points(player_data_df)
st.plotly_chart(minutes_to_points, use_container_width=True)

popularity_to_points = plot_popularity_to_points(player_data_df)
st.plotly_chart(popularity_to_points, use_container_width=True)