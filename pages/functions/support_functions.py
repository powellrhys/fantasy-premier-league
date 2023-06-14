import pandas as pd
import streamlit as st

def read_csv(path):

    df = pd.read_csv(path, index_col=False)

    return df

def summarise_manager_data(path):

    df = read_csv(path)
    df.columns = ['Key', 'Value']

    team_name = df.loc[df['Key'] == 'name', 'Value'].values[0]
    region = df.loc[df['Key'] == 'player_region_name', 'Value'].values[0]
    gameweek_points = df.loc[df['Key'] == 'summary_event_points', 'Value'].values[0]
    overall_points = df.loc[df['Key'] == 'summary_overall_points', 'Value'].values[0]
    overall_rank = df.loc[df['Key'] == 'summary_overall_rank', 'Value'].values[0]

    return team_name, region, gameweek_points, overall_points, overall_rank
