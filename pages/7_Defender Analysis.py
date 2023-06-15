import streamlit as st

from pages.functions.support_functions import \
    read_csv

from pages.functions.plots import plot_player_points_bar

st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
) 

st.markdown("# Defender Analyis")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Clean Sheets', 'Goals Conceded', 'Goals Scored', 
                                              'Assists', 'No. Starts', 'Yellow Cards', 'Red Cards']) 

defender_df = read_csv('data/players.csv')
defender_df = defender_df[defender_df['position'] == 'Defender']

with tab1:
    defender_df_cs = defender_df.sort_values(by=['clean_sheets'], ascending=False).head(15)
    fig = plot_player_points_bar(defender_df_cs, 'clean_sheets', 'Clean Sheets')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    defender_df_saves = defender_df.sort_values(by=['goals_conceded'], ascending=False).head(15)
    fig = plot_player_points_bar(defender_df_cs, 'goals_conceded', 'Goals Conceded')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    defender_df_saves = defender_df.sort_values(by=['goals_scored'], ascending=False).head(15)
    fig = plot_player_points_bar(defender_df_cs, 'goals_scored', 'Goals')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    defender_df_saves = defender_df.sort_values(by=['assists'], ascending=False).head(15)
    fig = plot_player_points_bar(defender_df_cs, 'assists', 'Assists')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    defender_df_saves = defender_df.sort_values(by=['starts'], ascending=False).head(15)
    fig = plot_player_points_bar(defender_df_cs, 'starts', 'Starts')
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    defender_df_saves = defender_df.sort_values(by=['yellow_cards'], ascending=True).head(15)
    fig = plot_player_points_bar(defender_df_cs, 'yellow_cards', 'Yellow Cards')
    st.plotly_chart(fig, use_container_width=True)

with tab7:
    defender_df_saves = defender_df.sort_values(by=['red_cards'], ascending=True).head(15)
    fig = plot_player_points_bar(defender_df_cs, 'red_cards', 'Red Cards')
    st.plotly_chart(fig, use_container_width=True)
