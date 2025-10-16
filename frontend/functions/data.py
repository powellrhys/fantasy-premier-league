# Import dependencies
from shared.functions import DatabaseConnector, PlayerRepository, LeagueRepository
import streamlit as st
import pandas as pd

@st.cache_data(ttl=3600)
def collect_player_data() -> pd.DataFrame:
    """
    Function to collect and cache player data from sql database
    """
    return PlayerRepository(db_connector=DatabaseConnector(source="Frontend")).read_dataframe()

@st.cache_data(ttl=3600)
def collect_managerial_league_data() -> pd.DataFrame:
    """
    Function to collect and cache managerial league data from sql database
    """
    return LeagueRepository(db_connector=DatabaseConnector(source="Frontend")).read_dataframe()
