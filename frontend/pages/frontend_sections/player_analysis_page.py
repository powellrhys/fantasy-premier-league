# Import dependencies
from streamlit_components.plot_functions import PlotlyPlotter
import streamlit as st
import pandas as pd

def render_player_analysis_page(df: pd.DataFrame) -> None:
    """
    Render the Player Analysis page in a Streamlit app with interactive controls and visualizations.

    The page allows users to:
    - Select player positions to filter the data.
    - Choose a metric to plot against total points.
    - Adjust sliders for top performers and budget constraints.
    - Visualize the filtered data using an interactive Plotly scatter plot with a trendline.

    Args:
        df (pd.DataFrame): A DataFrame containing player data, including columns such as
                           'position', 'now_cost', 'total_points', 'web_name', and other relevant metrics.

    Returns:
        None
    """
    # Render page title
    st.title("Player Analysis")

    # Define column object
    columns = st.columns([1, 1, 1, 1])

    # Render positions select box within first column
    with columns[0]:
        position_options = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
        position = st.selectbox(label="Position", options=position_options)

    # Render metric select box in second column
    with columns[1]:
        metric = st.selectbox(label="Metric", options=["Now Cost", "Minutes", "Selected By Percent"])

    # Render top performers slider in third column
    with columns[-2]:
        top_players = st.slider(label='Top Performers', min_value=20, max_value=50, value=30, step=1)

    # Render budget slider in final column
    with columns[-1]:
        budget = st.slider(label='Budget', min_value=0.0, max_value=15.0, value=15.0, step=0.1)

    # Filter data based on inputs
    df = df[df["position"] == position]
    df = df[df["now_cost"] <= budget]

    # Sort data by position and total points
    top_df = (
        df.sort_values(by=["position", "total_points"], ascending=[True, False])
        .groupby("position")
        .head(top_players)
    )

    # Configure page columns
    columns = st.columns([4, 1])

    # Render scatter plot with streamlit container within column 1
    with columns[0]:
        with st.container(border=True, height=500):
            st.plotly_chart(
                PlotlyPlotter(
                    df=top_df,
                    x=metric.replace(" ", "_").lower(),
                    y='total_points',
                    hover_data='web_name',
                    trendline='ols',
                    title=f"Breakdown of the top {top_players} Total Points per {metric}",
                    labels={
                        "total_points": "Total Points",
                        "position": "Position",
                        "web_name": "Player Name",
                        "now_cost": "Cost (£)",
                        "selected_by_percent": "Selected (%)",
                        "minutes": "Minutes"
                    }).plot_scatter())

    # Render streamlit container within final column
    with columns[-1]:
        with st.container(border=True, height=500):

            # Render player name select box
            player = st.selectbox(label="Drill Down Analysis", options=top_df["web_name"].tolist())

            # Construct photo url of player
            player_photo_url = "https://resources.premierleague.com/premierleague25/photos/players/110x140/" + \
                str(top_df[top_df["web_name"] == player]["photo"].values[0]).replace("jpg", "png")

            # Render player photo using streamlit markdown
            st.markdown(
                f"""
                <div style="text-align:center">
                    <br><br><img src="{player_photo_url}" height="300"><br>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Filter player dataframe down to player selected
    player_stats = top_df[top_df["web_name"] == player]

    # Define base metrics shared by each position type
    base_metrics = ["total_points", "selected_by_percent", "now_cost", "starts", "minutes"]

    # Construct a metric position map
    metric_position_map = {
        "Goalkeeper": ["clean_sheets", "goals_conceded", "saves", "penalties_saved", "penalties_missed"],
        "Defender": ["clean_sheets", "goals_conceded", "goals_scored", "assists", "yellow_cards", "red_cards",
                     "defensive_contribution_per_90"],
        "Midfielder": ["clean_sheets", "goals_conceded", "goals_scored", "assists", "yellow_cards", "red_cards",
                       "defensive_contribution_per_90"],
        "Forward": ["goals_scored", "assists", "yellow_cards", "red_cards", "defensive_contribution_per_90"]
    }

    # Add the base metrics to each position within the position map
    metric_position_map = {position: base_metrics + extras for position, extras in metric_position_map.items()}

    # Define metrics to render
    metrics = metric_position_map[position]

    # Define how many columns per row for each position
    columns_per_row_map = {"Goalkeeper": 5, "Defender": 6, "Midfielder": 6, "Forward": 5}

    # Default to 4 if not found (safe fallback)
    columns_per_row = columns_per_row_map.get(position, 4)

    # Within a container, render a subheader and subsequent player metrics
    with st.container(border=True):
        st.subheader(f"Drill Down Analysis of {player}")

        # Use % to wrap column metrics based on columns per row variable
        for i, metric_name in enumerate(metrics):
            if i % columns_per_row == 0:
                cols = st.columns(columns_per_row)
            with cols[i % columns_per_row]:
                st.metric(
                    label=metric_name.title().replace("_", " "),
                    value=player_stats[metric_name].values[0],
                    border=True
                )
