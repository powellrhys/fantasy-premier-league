# Import python and project dependencies
from frontend.pages.frontend_sections.home_page import render_home_page
from streamlit_components.ui_components import configure_page_config
from functions.data import collect_player_data, wake_up_database

# Set page config
configure_page_config(repository_name='fantasy-premier-league',
                      page_icon=":soccer:",
                      authentication_enabled=False)

# Ensure database is online
if wake_up_database():

    # Read player data from external source
    df = collect_player_data()

    # Render home page section
    render_home_page(df=df)
