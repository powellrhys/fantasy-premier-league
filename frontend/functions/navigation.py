# Import python dependencies
from shared.functions import Variables
import streamlit as st

def get_navigation(vars: Variables) -> st.navigation:
    """
    """
    # Construct pages dictionary
    pages = {
        "Home": [st.Page(page="pages/home.py", title="Home")],
        "Club & Player Analysis": [
            st.Page(page="pages/player_analysis.py", title="Player Analysis")
        ],
        "Chip Analysis": [
            st.Page(page="pages/chip_analysis.py", title="Chip Analysis")
        ],
    }

    # Construct streamlit navigation object
    nav = st.navigation(pages)

    return nav
