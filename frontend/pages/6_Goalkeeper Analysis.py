from pages.functions.plots import \
    plot_player_points_bar
from pages.functions.database import \
    connect_to_database

import streamlit as st
import pandas as pd

# Configure page config
st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
)

# UI components
st.markdown("# Goalkeeper Analyis")

# Configure page tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Clean Sheets', 'Saves Made', 'No. Starts',
                                                    'Penalty Saves', 'Goals Conceded', 'Yellow Cards',
                                                    'Red Cards'])

# Collect and filter data
cnxn, cursor = connect_to_database()
goalkeeper_df = pd.read_sql('Select * from fpl_player_data', cnxn)
goalkeeper_df = goalkeeper_df[goalkeeper_df['position'] == 'Goalkeeper']

# Generate and render plots
with tab1:
    goalkeeper_df_cs = goalkeeper_df.sort_values(by=['clean_sheets'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'clean_sheets', 'Clean Sheets')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    goalkeeper_df_saves = goalkeeper_df.sort_values(by=['saves'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_cs, 'saves', 'Saves')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    goalkeeper_df_starts = goalkeeper_df.sort_values(by=['starts'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_starts, 'starts', 'Starts')
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    goalkeeper_df_ps = goalkeeper_df.sort_values(by=['penalties_saved'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_ps, 'penalties_saved', 'Penalty Saves')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    goalkeeper_df_gc = goalkeeper_df.sort_values(by=['goals_conceded'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_gc, 'goals_conceded', 'Goal Conceded')
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    goalkeeper_df_yc = goalkeeper_df.sort_values(by=['yellow_cards'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_yc, 'yellow_cards', 'Yellow Cards')
    st.plotly_chart(fig, use_container_width=True)

with tab7:
    goalkeeper_df_rc = goalkeeper_df.sort_values(by=['red_cards'], ascending=False).head(15)
    fig = plot_player_points_bar(goalkeeper_df_rc, 'red_cards', 'Red Cards')
    st.plotly_chart(fig, use_container_width=True)
