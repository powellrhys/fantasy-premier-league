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

# Configure Page Config
st.set_page_config(
    page_title="Home",
    page_icon=":soccer:",
)

# Create empty json metadata file if no data previously collected
if not os.path.exists('data/last_updated.json'):

    json_object = {'general_data' : '',
                'my_team_data' : '',
                'all_player_data' : ''}
    
    with open("data/last_updated.json", "w") as outfile:
        json.dump(json_object, outfile)

# Opening JSON metadata file
with open('data/last_updated.json', 'r') as openfile:
    json_read = json.load(openfile)

# UI Components
st.title('Refresh Data')

general_data_toggle = st.checkbox('Update General Data', value=True)
st.write(f"Last Updated: :blue[{json_read['general_data']}]")

# Default value set to False as scraping is timing consuming
all_player_toggle = st.checkbox('Update All Player Data')
st.write(f"Last Updated: :blue[{json_read['all_player_data']}]")

my_team_toggle = st.checkbox('Update My Team Data', value=False)
st.write(f"Last Updated: :blue[{json_read['my_team_data']}]")

update_data_button = st.button('Update data')

# Execute scraping functions when button clicked
if update_data_button:
        with st.spinner('Collecting Data...'):
            
            # Collect current timestamp
            ct = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S") 

            # Update general data if toggle set to true
            if general_data_toggle:
                update_data()
                update_premier_league_table()
                json_read['general_data'] = ct

            # Update user team data if toggle set to true   
            if my_team_toggle:
                update_my_team_data()
                json_read['my_team_data'] = ct 
               
            # Update all player data if toggle set to true
            if all_player_toggle:
                 update_all_player_data()
                 json_read['all_player_data'] = ct

            # Update json metadata file
            with open("data/last_updated.json", "w") as outfile:
                json.dump(json_read, outfile)

            # Refresh page
            st.experimental_rerun()
