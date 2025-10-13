# Import dependencies
from streamlit_components.plot_functions import PlotlyPlotter
from functions.mapping import team_colour_map
import streamlit as st
import pandas as pd

def render_position_analysis_page(df: pd.DataFrame, is_goalkeeper: bool = False) -> None:
    """
    Render an analysis page for either goalkeepers or outfield players.

    Args:
        df (pd.DataFrame): The player dataset.
        is_goalkeeper (bool): If True, shows goalkeeper metrics only.
                              Otherwise, shows outfield player metrics.
    """
    # If goalkeeper page - render goalkeeper section
    if is_goalkeeper:

        # Render page title and define column structure
        st.title("Goalkeeper Analysis")
        columns = st.columns([1, 3, 1])

        # Render metric select box in first column

        with columns[0]:
            metric = st.selectbox(label="Metric",
                                  options=['Clean Sheets', 'Saves', 'Starts', 'Penalties Saved',
                                           'Goals Conceded', 'Yellow Cards', 'Red Cards'])

        # Filter data by position
        df = df[df["position"] == "Goalkeeper"]

    else:
        # Render outfield player title and define page columns
        st.title("Outfield Player Analysis")
        columns = st.columns([1, 1, 3])

        # Render position select box in first column
        with columns[0]:
            position = st.selectbox(label="Position", options=["Defender", "Midfielder", "Forward"])

        # Render metric select box in second column
        with columns[1]:
            metric = st.selectbox(label="Metric",
                                  options=['Goals Scored', 'Assists', 'Starts', 'Clean Sheets', 'Goals Conceded',
                                           'Penalties Missed', 'Yellow Cards', 'Red Cards'])

        # Filter data by position
        df = df[df["position"] == position]

    # Sort and take top 15
    df = df.sort_values(by=[metric.lower().replace(" ", "_")], ascending=False).head(15)

    # Generate bar plot
    fig = PlotlyPlotter(
        df,
        x='second_name',
        y=metric.lower().replace(" ", "_"),
        text='team',
        color='team',
        color_discrete_map=team_colour_map,
        labels={
            "second_name": "Name",
            metric.lower().replace(" ", "_"): metric.replace("_", " ").capitalize(),
            "team": "Team"
        }
    ).plot_bar()

    # Update figure config
    fig.update_xaxes(categoryorder='total descending')
    fig.update_layout(showlegend=False)
    fig.update_traces(marker_line_color='black', marker_line_width=1)

    with st.container():

        # Render plot
        st.plotly_chart(fig)
