from pages.functions.support_functions import \
    read_csv
from pages.functions.plots import \
    plot_bar_historic_season, \
    plot_bar_historic_player

import streamlit as st

# Configure page config
st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
)

# UI components
st.markdown("# Historic Analysis")

# Collect list of user leages
season_df = read_csv('data_historic/views/seasonal_position.csv')
player_df = read_csv('data_historic/views/all_time_player_performance.csv')
player_df['label'] = player_df['season_x'] + ' - ' + player_df['name']

tab1, tab2, tab3, tab4 , tab5, tab6 = st.tabs(['Goals Scored', 'Assists', 'Total Points',
                                               'Seasonal Goal Scorers', 'SeasonalAssists',
                                               'Seasonal Total Points'])

# Generate and render plots
with tab1:
    fig = plot_bar_historic_season(season_df, 'goals_scored', 'Goals Scored')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = plot_bar_historic_season(season_df, 'assists', 'Assists')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    fig = plot_bar_historic_season(season_df, 'total_points', 'Total Points')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    slider_gs = st.slider('Number of Top Performers', 10, 25, 15, key='tab4')

    player_df_gs = player_df.sort_values(by=['goals_scored'], ascending=False).head(slider_gs)
    fig = plot_bar_historic_player(player_df_gs, 'goals_scored', 'Goals Scored')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    slider_a = st.slider('Number of Top Performers', 10, 25, 15, key='tab5')

    player_df_a = player_df.sort_values(by=['assists'], ascending=False).head(slider_a)
    fig = plot_bar_historic_player(player_df_a, 'assists', 'Assists')
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    slider_tp = st.slider('Number of Top Performers', 10, 25, 15, key='tab6')

    player_df_tp = player_df.sort_values(by=['total_points'], ascending=False).head(slider_tp)
    fig = plot_bar_historic_player(player_df_tp, 'total_points', 'Total Points')
    st.plotly_chart(fig, use_container_width=True)
