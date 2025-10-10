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
                           'position', 'now_cost', 'total_points', 'second_name', and other relevant metrics.

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
        positions = [st.selectbox(label="Position", options=position_options)]

    # Render metric select box in second column
    with columns[1]:
        metric = st.selectbox(label="Metric", options=["now_cost", "minutes", "selected_by_percent"])

    # Render top performers slider in third column
    with columns[-2]:
        top_players = st.slider(label='Top Performers', min_value=20, max_value=50, value=30, step=1)

    # Render budget slider in final column
    with columns[-1]:
        budget = st.slider(label='Budget', min_value=0.0, max_value=15.0, value=15.0, step=0.1)

    # Filter data based on inputs
    df = df[df["position"].isin(positions)]
    df = df[df["now_cost"] <= budget]

    # Sort data by position and total points
    top_df = (
        df.sort_values(by=["position", "total_points"], ascending=[True, False])
        .groupby("position")
        .head(top_players)
    )

    # Render plot within expander
    with st.container(expanded=True):
        st.plotly_chart(
            PlotlyPlotter(
                df=top_df,
                x=metric,
                y='total_points',
                hover_data='second_name',
                trendline='ols',
                labels={
                    "total_points": "Total Points",
                    "position": "Position",
                    "second_name": "Player Name",
                    "now_cost": "Cost (£)",
                    "selected_by_percent": "Selected (%)",
                    "minutes": "Minutes"
                }).plot_scatter())
