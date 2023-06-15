import streamlit as st
import pandas as pd

from pages.functions.support_functions import \
    read_csv, \
    find_player_index_in_list

st.set_page_config(
    page_title="Chip Analysis",
    page_icon=":soccer:",
)   

player_data_df = read_csv('data/players.csv')
current_team = read_csv('data/my_team.csv')['0'].to_list()

goal_keeper_names = player_data_df[player_data_df['position'] == 'Goalkeeper']['second_name'].to_list()
defender_names = player_data_df[player_data_df['position'] == 'Defender']['second_name'].to_list()
midfielder_names = player_data_df[player_data_df['position'] == 'Midfielder']['second_name'].to_list()
forward_names = player_data_df[player_data_df['position'] == 'Forward']['second_name'].to_list()

index = find_player_index_in_list(current_team, goal_keeper_names, defender_names, midfielder_names, forward_names)

st.markdown("# Update Team")

gk0, gk1, gk2, gk3= st.columns([1,2,2,1])

with gk1:
    gk1 = st.selectbox('Goalkeeper 1', tuple(goal_keeper_names), key='gk1', index=index[0])

with gk2:
    gk2 = st.selectbox('Goalkeeper 2', tuple(goal_keeper_names),key='gk2', index=index[1])

def1, def2, def3, def4, def5 = st.columns(5)

with def1:
    def1 = st.selectbox('Defender 1', tuple(defender_names), key='def1', index=index[2])

with def2:
    def2 = st.selectbox('Defender 2', tuple(defender_names), key='def2', index=index[3])

with def3:
    def3 = st.selectbox('Defender 3', tuple(defender_names), key='def3', index=index[4])

with def4:
    def4 = st.selectbox('Defender 4', tuple(defender_names), key='def4', index=index[5])

with def5:
    def5 = st.selectbox('Defender 5', tuple(defender_names), key='def5', index=index[6])

mid1, mid2, mid3, mid4, mid5 = st.columns(5)

with mid1:
    mid1 = st.selectbox('Miplayer 1', tuple(midfielder_names), key='mid1', index=index[7])

with mid2:
    mid2 = st.selectbox('Miplayer 2', tuple(midfielder_names), key='mid2', index=index[8])

with mid3:
    mid3 = st.selectbox('Miplayer 3', tuple(midfielder_names), key='mid3', index=index[9])

with mid4:
    mid4 = st.selectbox('Miplayer 4', tuple(midfielder_names), key='mid4', index=index[10])

with mid5:
    mid5 = st.selectbox('Miplayer 5', tuple(midfielder_names), key='mid5', index=index[11])

fow0, fow1, fow2, fow3, fow4 = st.columns([1,2,2,2,1])

with fow1:
    fow1 = st.selectbox('Forward 1', tuple(forward_names), key='fow1', index=index[12])

with fow2:
    fow2 = st.selectbox('Forward 2', tuple(forward_names), key='fow2', index=index[13])

with fow3:
    fow3 = st.selectbox('Forward 3', tuple(forward_names), key='fow3', index=index[14])

my_team = [gk1, gk2, def1, def2, def3, def4, def5, mid1, mid2, mid3, mid4, mid5, fow1, fow2, fow3]
my_team_df = pd.Series(my_team)

button0, button1, button2, button3 = st.columns([1,1,1,1])

with button1:

    if st.button('Update My Team'):
        with st.spinner('Collecting Data...'):
            my_team_df.to_csv('data/my_team.csv')

with button2:
    if st.button('Collected Team Data'):
        with st.spinner('Collecting Data...'):
            my_team_df.to_csv('data/my_team.csv')
