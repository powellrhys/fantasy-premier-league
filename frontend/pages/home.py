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
        Welcome to FPL Insights, a data-driven platform designed to optimize decision-making in Fantasy Premier League
        management. This application leverages statistical models, performance metrics, and fixture analytics to
        provide a comprehensive overview of the factors that influence player and team performance each gameweek.
        Whether you are seeking to refine your transfer strategy, identify value players, or maximize chip efficiency,
        FPL Insights offers the analytical tools to support your decision-making process.

        Through interactive dashboards and visualizations, users can explore key indicators such as expected
        goals (xG), expected assists (xA), fixture difficulty ratings (FDR), and ownership trends. Each visualization
        is crafted to translate complex datasets into actionable insights, allowing managers to compare players, assess
        form, and anticipate emerging trends across the league. Real-time data integration ensures that all metrics
        reflect the most current developments in the Premier League.

        FPL Insights aims to bridge the gap between intuition and analytics by providing a structured approach to team
        management. With advanced filtering, player comparison, and predictive modeling features, the platform enables
        evidence-based decision-making at every stage of the season. The result is a professional-grade toolkit that
        empowers users to make informed, strategic choices — and ultimately, to enhance performance and consistency in
        Fantasy Premier League competition.
        """
    )
