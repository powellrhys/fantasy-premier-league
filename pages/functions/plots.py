from pages.functions.support_functions import read_csv
import plotly.express as px

def plot_cost_to_points(df):

    fig = px.scatter(df, x='now_cost', 
                    y='total_points', 
                    color='position', 
                    hover_data='second_name', 
                    trendline='ols',
                    labels={
                        "now_cost" : "Player Cost",
                        "total_points" : "Total Points",
                        "position" : "Position",
                        "second_name" : "Name"
                    })
    
    return fig

def plot_minutes_to_points(df):

    fig = px.scatter(df, x='minutes', 
                    y='total_points', 
                    color='position', 
                    hover_data='second_name', 
                    trendline='ols',
                    labels={
                        "minutes" : "Minutes Played",
                        "total_points" : "Total Points",
                        "position" : "Position",
                        "second_name" : "Name"
                    })
    
    return fig