# Import dependencies
from frontend.pages.frontend_sections.position_analysis_page import render_position_analysis_page
from streamlit_components.ui_components import configure_page_config
from shared.functions import BlobStorage

# Set page config
configure_page_config(repository_name='fantasy-premier-league',
                      page_icon=":soccer:",
                      authentication_enabled=False)

# Read player data from external source
df = BlobStorage().read_csv_from_blob(file_name="player_data.csv")

render_position_analysis_page(df=df, is_goalkeeper=True)
