# Import python and project dependencies
from streamlit_components.ui_components import configure_page_config
import streamlit as st

# Set page config
configure_page_config(repository_name='fantasy-premier-league',
                      page_icon=":soccer:",
                      authentication_enabled=False)

# Render page title
st.title("Fantasy Premier League Dashboard")

# Render container
with st.container(border=True):

    # Render application overview paragraph
    st.write(
        """
        """
    )
