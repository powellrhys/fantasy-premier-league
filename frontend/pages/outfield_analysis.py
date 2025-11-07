# Import dependencies
from frontend.pages.frontend_sections.position_analysis_page import render_position_analysis_page
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

    # Render outfield analysis page
    render_position_analysis_page(df=df, is_goalkeeper=False)
