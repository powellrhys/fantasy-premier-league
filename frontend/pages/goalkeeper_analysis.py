# Import dependencies
from frontend.pages.frontend_sections.position_analysis_page import render_position_analysis_page
from streamlit_components.ui_components import configure_page_config
from functions.data import collect_player_data

# Set page config
configure_page_config(repository_name='fantasy-premier-league',
                      page_icon=":soccer:",
                      authentication_enabled=False)

# Read player data from external source
df = collect_player_data()

# Render goalkeeper page
render_position_analysis_page(df=df, is_goalkeeper=True)
