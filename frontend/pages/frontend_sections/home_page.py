# Import dependencies
import streamlit as st
import pandas as pd

def render_home_page(df: pd.DataFrame) -> None:
    """
    Render the Fantasy Premier League dashboard home page.

    Displays an overview of the FPL Insights application and the current 
    Dream Team, including player photos, stats, and key performance metrics.
    
    Args:
        df (pd.DataFrame): DataFrame containing player data from the 
            Fantasy Premier League API.
    """
    # Render page title
    st.title("Fantasy Premier League Dashboard")

    # Render container
    with st.container(border=True):

        # Render application overview paragraph
        st.write(
            """
            Welcome to FPL Insights, a data-driven platform designed to optimize decision-making in Fantasy Premier
            League management. This application leverages statistical models, performance metrics, and fixture
            analytics to provide a comprehensive overview of the factors that influence player and team performance
            each gameweek. Whether you are seeking to refine your transfer strategy, identify value players, or
            maximize chip efficiency, FPL Insights offers the analytical tools to support your decision-making process.

            Through interactive dashboards and visualizations, users can explore key indicators such as expected
            goals (xG), expected assists (xA), fixture difficulty ratings (FDR), and ownership trends. Each
            visualization is crafted to translate complex datasets into actionable insights, allowing managers to
            compare players, assess form, and anticipate emerging trends across the league. Real-time data integration
            ensures that all metrics reflect the most current developments in the Premier League.

            FPL Insights aims to bridge the gap between intuition and analytics by providing a structured approach to
            team management. With advanced filtering, player comparison, and predictive modeling features, the platform
            enables evidence-based decision-making at every stage of the season. The result is a professional-grade
            toolkit that empowers users to make informed, strategic choices — and ultimately, to enhance performance
            and consistency in Fantasy Premier League competition.
            """
        )

    # Render second title
    st.title("Current FPL Dream Team")

    # Filter dataframe to only include dream team players
    dream_df = df[df["in_dreamteam"]]

    # Append photo url to photo file name
    dream_df["photo"] = dream_df["photo"] = \
        "https://resources.premierleague.com/premierleague25/photos/players/110x140/" + df["photo"]

    # Replace jpg file type with png
    dream_df["photo"] = dream_df["photo"].str.replace(".jpg", ".png")

    # Sort data by total points scored and reset the index
    dream_df = dream_df.sort_values(by="total_points", ascending=False)
    dream_df = dream_df.reset_index()

    # Configure and render 11 columns in a container object
    with st.container(border=True):
        player_cols = st.columns(11)

        # Iterate through each dream team player and render markdown of player photo and stats overview
        for i, row in dream_df.iterrows():
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
