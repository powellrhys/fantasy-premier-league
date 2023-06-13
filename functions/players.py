import requests
import pandas as pd

def collect_player_data():

    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    r = requests.get(url)
    json = r.json()

    elements_df = pd.DataFrame(json['elements'])
    elements_types_df = pd.DataFrame(json['element_types'])
    teams_df = pd.DataFrame(json['teams'])

    slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]
    slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
    slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
    slim_elements_df['value'] = slim_elements_df.value_season.astype(float)

    slim_elements_df = slim_elements_df[['second_name','team','position','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]

    slim_elements_df.to_csv('data/players.csv')
