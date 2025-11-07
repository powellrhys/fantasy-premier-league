# Import python and project dependencies
from pages.frontend_sections.chip_analysis_page import render_chip_analysis_page
from functions.data import collect_managerial_league_data, wake_up_database
from streamlit_components.ui_components import configure_page_config
from shared.functions import Variables
import streamlit as st

# Set page config
configure_page_config(repository_name='fantasy-premier-league',
                      page_icon=":soccer:")

# Ensure user is authenticated to use application
if not st.user.is_logged_in:
    st.login('auth0')

st.title("Chip Analysis")

# If user logged in, render streamlit content
if st.user.is_logged_in and st.user["name"] in Variables(source="frontend").privileged_users:

    # Ensure database is online
    if wake_up_database():

        # Read in leagues_data from external source
        leagues_df = collect_managerial_league_data()

        # Render chip analysis section
        render_chip_analysis_page(leagues_df=leagues_df)

else:
    # Handle unauthenticated user
    st.error(
        f"""
        **{st.user["name"]}** does not have access to this page!!

        The following page contains information specific to privileged users of the project
        and therefore cannot be viewed
        """
    )
