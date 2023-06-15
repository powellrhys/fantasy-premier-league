from pages.functions.support_functions import read_csv
from pages.functions.plots import *

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
)

list_of_leagues = read_csv('data_leagues/list_of_leagues.csv')['0'].to_list()

league_selected = st.sidebar.radio(
    "League to Analyse",
    tuple(list_of_leagues)).replace('/', '_').replace(' ', '_').lower()

league_data_df = read_csv(f'data_leagues/{league_selected}.csv')

st.markdown("# Chip Analysis")

df_melted = pd.melt(league_data_df, id_vars=['player_name','rank'], value_vars=['Bench Boost', 'Free Hit', 'Triple Captain'])
fig = plot_bar_chips_used(df_melted)
st.plotly_chart(fig, use_container_width=True)
