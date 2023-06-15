import streamlit as st

from pages.functions.support_functions import \
    read_csv

from pages.functions.plots import plot_player_points_bar

st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
) 

st.markdown("# Goalkeeper Analyis")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Clean Sheets', 'Saves Made', 'No. Starts',
                                              'Penalty Saves', 'Goals Conceded', 'Yellow Cards',
                                              'Red Cards']) 

goalkeeper_df = read_csv('data/players.csv')
goalkeeper_df = goalkeeper_df[goalkeeper_df['position'] == 'Goalkeeper']

with tab1:
    goalkeeper_df_cs = goalkeeper_df.sort_values(by=['clean_sheets'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'clean_sheets', 'Clean Sheets')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    goalkeeper_df_saves = goalkeeper_df.sort_values(by=['saves'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'saves', 'Saves')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    goalkeeper_df_saves = goalkeeper_df.sort_values(by=['starts'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'starts', 'Starts')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    goalkeeper_df_saves = goalkeeper_df.sort_values(by=['penalties_saved'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'penalties_saved', 'Penalty Saves')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    goalkeeper_df_saves = goalkeeper_df.sort_values(by=['goals_conceded'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'goals_conceded', 'Goal Conceded')
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    goalkeeper_df_saves = goalkeeper_df.sort_values(by=['yellow_cards'], ascending=True).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'yellow_cards', 'Yellow Cards')
    st.plotly_chart(fig, use_container_width=True)

with tab7:
    goalkeeper_df_saves = goalkeeper_df.sort_values(by=['red_cards'], ascending=True).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'red_cards', 'Red Cards')
    st.plotly_chart(fig, use_container_width=True)
