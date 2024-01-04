from pages.functions.support_functions import \
    read_csv
from pages.functions.plots import \
    plot_bar_chips_used

from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import os

# Configure page config
st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
)

load_dotenv()

col1, col2, = st.columns([3,2])

with col1:
    # UI component
    st.markdown("# Chip Analysis")

with col2:
    pw = st.text_input('Password', type='password')

if pw != os.getenv('password'):

    st.text('Login to see league chip usage breakdown')

else:

    # Collect list of user leages
    list_of_leagues = read_csv('data_leagues/list_of_leagues.csv')['0'].to_list()

    league_selected = st.selectbox(
        label='League', 
        options=tuple(list_of_leagues)).replace('/', '_').replace(' ', '_').lower()

    # Read leage data for selected leage
    league_data_df = read_csv(f'data_leagues/{league_selected}.csv')

    # Melt, generate and render results
    df_melted = pd.melt(league_data_df, id_vars=['player_name','rank'], value_vars=['Bench Boost', 'Free Hit', 'Triple Captain'])
    fig = plot_bar_chips_used(df_melted)
    st.plotly_chart(fig, use_container_width=True)
