from pages.functions.plots import \
    plot_bar_chips_used

from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import requests
import os

# Configure page config
st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
)

load_dotenv()

col1, col2, = st.columns([3, 2])

with col1:
    # UI component
    st.markdown("# Chip Analysis")

with col2:
    pw = st.text_input('Password', type='password')

if pw != os.getenv('password'):

    st.text('Login to see league chip usage breakdown')

else:

    # Collect list of user leages
    response = requests.get(f"{os.getenv('api_url')}/leagues?api_key={os.getenv('password')}")
    leagues_df = pd.DataFrame(response.json())

    list_of_leagues = leagues_df['league_name'].unique()
    league_selected = st.selectbox(
        label='League',
        options=tuple(list_of_leagues))

    league_data_df = leagues_df[leagues_df['league_name'] == league_selected].rename(columns={
        'bench_boost': 'Bench Boost',
        'free_hit': 'Free Hit',
        'triple_c': 'Triple Captain'})

    # Melt, generate and render results
    df_melted = pd.melt(league_data_df, id_vars=['player_name', 'league_rank'],
                        value_vars=['Bench Boost', 'Free Hit', 'Triple Captain'])
    fig = plot_bar_chips_used(df_melted)
    st.plotly_chart(fig, use_container_width=True)
