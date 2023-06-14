from pages.functions.support_functions import read_csv
from pages.functions.plots import *

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Player Value Analysis",
    page_icon=":soccer:",
)

league_data_df = read_csv('data_leagues/creigiau_rocks_2022_23_season..csv')

st.markdown("# League Analyis")

df_melted = pd.melt(league_data_df, id_vars=['player_name','rank'], value_vars=['Bench Boost', 'Free Hit', 'Triple Captain'])
fig = plot_bar_chips_used(df_melted)
st.plotly_chart(fig, use_container_width=True)
