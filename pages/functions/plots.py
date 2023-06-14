from pages.functions.colour_mapping import team_colour_map
import plotly.express as px

def plot_scatter_player_points(df, x, xlabel):
    fig = px.scatter(df, 
                    x=x, 
                    y='total_points', 
                    color='position', 
                    hover_data='second_name', 
                    trendline='ols',
                    labels={
                        x : xlabel,
                        "total_points" : "Total Points",
                        "position" : "Position",
                        "second_name" : "Name"
                    })
    
    return fig

def plot_bar_chips_used(df):
    fig = px.bar(df, 
                x='player_name', 
                y='value',
                color='variable',
                labels={
                    "player_name" : "Name",
                    "value" : "Chips Played",
                    "variable" : 'Chips'
                })

    return fig

def plot_points_per_team(df):
    fig = px.bar(df, 
                x='team', 
                y='total_points',
                color='position',
                labels={
                    "team" : "Team",
                    "total_points" : "Total Points",
                    "position" : "Position"
                })
    fig.update_layout(xaxis = {"categoryorder":"total descending"})

    return fig

def plot_player_points_bar(df, y, y_label):
    fig = px.bar(df, 
                x='second_name', 
                y=y,
                text='team',
                color='team',
                color_discrete_map = team_colour_map,
                labels={
                    "second_name" : "Name",
                    y : y_label,
                    "team" : "Team"
                })
    fig.update_xaxes(categoryorder='total descending') 
    fig.update_layout(showlegend=False)
    fig.update_traces(marker_line_color = 'black',
                    marker_line_width = 1)

    return fig