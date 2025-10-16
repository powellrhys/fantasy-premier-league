# Import python and project dependencies
from streamlit_components.ui_components import configure_page_config
from functions.data import collect_player_data
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

st.title("Current FPL Dream Team")

# Read player data from external source
df = collect_player_data()
df = df[df["in_dreamteam"]]
df["photo"] = df["photo"] = "https://resources.premierleague.com/premierleague25/photos/players/110x140/" + df["photo"]
df["photo"] = df["photo"].str.replace(".jpg", ".png")
df = df.sort_values(by="total_points", ascending=False)
df = df.reset_index()

with st.container(border=True):
    player_cols = st.columns(11)

    for i, row in df.iterrows():

        player_name = row["web_name"]
        photo_url = row["photo"]
        total_points = row["total_points"]

        with player_cols[i % 11]:
            st.markdown(
                f"""
                <div style="text-align:center">
                    <span style="font-weight:bold">{row["web_name"]}</span><br>
                    <span>{row["team"]}</span><br>
                    <img src="{row["photo"]}" width="100"><br><br>
                    <span>Total points: <b>{row["total_points"]}</b></span><br>
                    <span>Selected By: <b>{row["selected_by_percent"]} %</b></span>
                    <span>Current Cost: <b>{row["now_cost"]}</b></span><br>
                    <span>Position: <b>{row["position"]}</b></span>
                </div>
                """,
                unsafe_allow_html=True
            )
