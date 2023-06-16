from pages.functions.support_functions import summarise_manager_data
from update_data import \
    update_data, \
    update_my_team_data, \
    update_all_player_data, \
    update_premier_league_table

import streamlit as st
import datetime
import json
import os

st.set_page_config(
    page_title="Home",
    page_icon=":soccer:",
)

team_name, region, gameweek_points, overall_points, overall_rank = summarise_manager_data('data/manager_summary.csv')

if not os.path.exists('data/last_updated.json'):

    json_object = {'general_data' : '',
                'my_team_data' : '',
                'all_player_data' : ''}
    
    with open("data/last_updated.json", "w") as outfile:
        json.dump(json_object, outfile)

# Opening JSON file
with open('data/last_updated.json', 'r') as openfile:

    # Reading from json file
    json_read = json.load(openfile)

st.title('Refresh Data')

general_data_toggle = st.checkbox('Update General Data', value=True)
st.write(f"Last Updated: :blue[{json_read['general_data']}]")

my_team_toggle = st.checkbox('Update My Team Data', value=True)
st.write(f"Last Updated: :blue[{json_read['my_team_data']}]")

all_player_toggle = st.checkbox('Update All Player Data')
st.write(f"Last Updated: :blue[{json_read['all_player_data']}]")

update_data_button = st.button('Update data')

if update_data_button:
        with st.spinner('Collecting Data...'):

            ct = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S") 

            if general_data_toggle:
                update_data()
                update_premier_league_table()
                json_read['general_data'] = ct
                
            if my_team_toggle:
                update_my_team_data()
                json_read['my_team_data'] = ct 
               
            if all_player_toggle:
                 update_all_player_data()
                 json_read['all_player_data'] = ct

            with open("data/last_updated.json", "w") as outfile:
                json.dump(json_read, outfile)

            st.experimental_rerun()
