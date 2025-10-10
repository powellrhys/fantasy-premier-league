# Import dependencies
from streamlit_components.plot_functions import PlotlyPlotter
import streamlit as st
import pandas as pd

def render_player_analysis_page(df: pd.DataFrame) -> None:
    """
    """
    # Render page title
    st.title("Player Analysis")

    columns = st.columns([1, 1, 1, 1])

    with columns[0]:
        position_options = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
        positions = [st.selectbox(label="Position", options=position_options)]

    with columns[1]:
        metric = st.selectbox(label="Metric", options=["now_cost", "minutes", "selected_by_percent"])

    with columns[-2]:
        top_players = st.slider(label='Top Performers', min_value=20, max_value=50, value=30, step=1)

    with columns[-1]:
        budget = st.slider(label='Budget', min_value=0.0, max_value=15.0, value=15.0, step=0.1)

    df = df[df["position"].isin(positions)]
    df = df[df["now_cost"] <= budget]

    top_df = (
        df.sort_values(by=["position", "total_points"], ascending=[True, False])
        .groupby("position")
        .head(top_players)
    )

    # Render plot within expander
    with st.expander(label="", expanded=True):
        st.plotly_chart(
            PlotlyPlotter(
                df=top_df,
                x=metric,
                y='total_points',
                # color='position',
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
