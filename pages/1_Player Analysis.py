import streamlit as st

from pages.functions.support_functions import read_csv
from pages.functions.plots import plot_cost_to_points

st.set_page_config(
    page_title="Player Analysis",
    page_icon=":soccer:",
)

st.markdown("# Plotting Demo")

cost_to_points = plot_cost_to_points()
st.plotly_chart(cost_to_points, use_container_width=True)
