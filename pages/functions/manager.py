import requests
import pandas as pd

def collect_manager_data(manager_id):

    url = f'https://fantasy.premierleague.com/api/entry/{manager_id}/' 

    r = requests.get(url)
    json = r.json()

    json.pop('leagues')

    df = pd.Series(json)

    df.to_csv('data/manager_summary.csv')
