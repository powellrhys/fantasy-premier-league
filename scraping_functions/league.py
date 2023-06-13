import requests
import pandas as pd

def collect_league_data(league_id):

    url = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings' 

    r = requests.get(url)
    json = r.json()

    league_name = json['league']['name'].replace('/', '_').replace(' ', '_').lower()

    df = pd.DataFrame(json['standings']['results'])

    df.to_csv(f'data_league/{league_name}.csv')
