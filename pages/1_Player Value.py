from pages.functions.support_functions import read_csv
from pages.functions.ui_components import position_checkbox
from pages.functions.plots import \
    plot_scatter_player_points, \
    plot_player_points_bar

import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

player_data_df = read_csv('data/players.csv')

st.markdown("# Player Value Analyis")

position_filter = position_checkbox('player_value_page')

budget_filter = st.sidebar.slider(label='Budget',
                          min_value=0.0, 
                          max_value=14.0, 
                          value=14.0, 
                          step=0.1)

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Player Cost', 'Minutes Played', 
                                        'Player Popularity', 'Top Performers',
                                        'Top Value Performers'])

player_data_df['points_per_cost'] = player_data_df['total_points'] / player_data_df['now_cost']
player_data_df = player_data_df[player_data_df['position'].isin(position_filter)]
player_data_df = player_data_df[player_data_df['now_cost'] <= budget_filter]

top_player_data_df = player_data_df.sort_values(by=['total_points'], ascending=False).head(15)
top_player_data_df_normalised = player_data_df.sort_values(by=['points_per_cost'], ascending=False).head(15)


with tab1:
    cost_to_points = plot_scatter_player_points(player_data_df, 'now_cost', 'Player Cost')
    st.plotly_chart(cost_to_points, use_container_width=True)

with tab2:
    minutes_to_points = plot_scatter_player_points(player_data_df, 'minutes', 'Minutes Played')
    st.plotly_chart(minutes_to_points, use_container_width=True)

with tab3:
    popularity_to_points = plot_scatter_player_points(player_data_df, 'selected_by_percent', 'Selected By (%)')
    st.plotly_chart(popularity_to_points, use_container_width=True)

with tab4:
    top_value_players = plot_player_points_bar(top_player_data_df, 'total_points', 'Total Points')
    st.plotly_chart(top_value_players, use_container_width=True)

with tab5:
    top_value_player_normalised = plot_player_points_bar(top_player_data_df_normalised, 'points_per_cost', 'Points per Unit Cost')
    st.plotly_chart(top_value_player_normalised, use_container_width=True)
