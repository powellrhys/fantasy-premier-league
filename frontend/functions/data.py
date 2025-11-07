# Import dependencies
from shared.functions import DatabaseConnector, PlayerRepository, LeagueRepository
import streamlit as st
import pandas as pd
import time

def wake_up_database() -> bool:
    """
    Attempts to connect to the SQL Server by executing a simple test query.

    The function retries up to five times, waiting 10 seconds between each attempt.
    Connection status is displayed in Streamlit using a spinner and status messages.
    If the connection succeeds, the function returns True. Otherwise, it displays
    an error message in Streamlit and returns False.

    Returns:
        bool: True if the SQL Server connection is successful, False otherwise.
    """
    # Create sql server engine object
    db_connector = DatabaseConnector(source="Frontend")
    engine = db_connector.get_engine()

    # Create a placeholder to update info messages
    placeholder = st.empty()

    # Loop 5 times to try and turn sql server online
    with st.spinner(text="Backend Server Offline. Attempting to reconnect backend..."):
        for i in range(5):
            try:
                pd.read_sql("SELECT 1", engine)
                placeholder.empty()
                return True
            except Exception as e:
                placeholder.info(f"SQL Server Offline [Server Start Up Attempts - {i + 1}] - {e}")

            # Sleep for 10 seconds before trying to turn server online again
            time.sleep(10)

    # If we reach here, all attempts failed, remove last info message and log error
    placeholder.empty()
    st.error("SQL Server Offline - Try again later")
    return False


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
