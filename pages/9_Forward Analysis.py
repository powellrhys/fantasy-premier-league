import streamlit as st

from pages.functions.support_functions import \
    read_csv

from pages.functions.plots import plot_player_points_bar

st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
) 

st.markdown("# Forward Analyis")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Goals Scored', 'Assists', 'No. Starts', 
                                                    'Clean Sheets', 'Penalties Missed', 'Yellow Cards',
                                                    'Red Cards']) 

forward_df = read_csv('data/players.csv')
forward_df = forward_df[forward_df['position'] == 'Forward']

with tab1:
    forward_df_gs = forward_df.sort_values(by=['goals_scored'], ascending=False).head(15)
    fig = plot_player_points_bar(forward_df_gs, 'goals_scored', 'Goals')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    forward_df_a = forward_df.sort_values(by=['assists'], ascending=False).head(15)
    fig = plot_player_points_bar(forward_df_a, 'assists', 'Assists')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    forward_df_starts = forward_df.sort_values(by=['starts'], ascending=False).head(15)
    fig = plot_player_points_bar(forward_df_starts, 'starts', 'Starts')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    forward_df_gc = forward_df.sort_values(by=['goals_conceded'], ascending=False).head(15)
    fig = plot_player_points_bar(forward_df_gc, 'goals_conceded', 'Goals Conceded')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    forward_df_pm = forward_df.sort_values(by=['penalties_missed'], ascending=False).head(15)
    fig = plot_player_points_bar(forward_df_pm, 'penalties_missed', 'Penalties Missed')
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    forward_df_yc = forward_df.sort_values(by=['yellow_cards'], ascending=False).head(15)
    fig = plot_player_points_bar(forward_df_yc, 'yellow_cards', 'Yellow Cards')
    st.plotly_chart(fig, use_container_width=True)

with tab7:
    forward_df_rc = forward_df.sort_values(by=['red_cards'], ascending=False).head(15)
    fig = plot_player_points_bar(forward_df_rc, 'red_cards', 'Red Cards')
    st.plotly_chart(fig, use_container_width=True)
