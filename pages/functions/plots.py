from pages.functions.support_functions import read_csv
import plotly.express as px

def plot_cost_to_points():

    df = read_csv('data/players.csv')

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