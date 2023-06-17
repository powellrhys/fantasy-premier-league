import pandas as pd
import requests

def collect_manager_data(manager_id):

    # Endpoint url
    url = f'https://fantasy.premierleague.com/api/entry/{manager_id}/' 

    # Read endpoint data
    r = requests.get(url)
    json = r.json()

    # Remove leagues data
    json.pop('leagues')

    # Create pandas series from data retrieved
    df = pd.Series(json)

    # Write series to storage
    df.to_csv('data/manager_summary.csv')
