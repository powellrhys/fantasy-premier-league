import requests
import pandas as pd

def collect_manager_chip_data(manager_id):

    url = f' https://fantasy.premierleague.com/api/entry/{manager_id}/history/'

    r = requests.get(url)
    json = r.json()

    chip_filter = ['bboost', 'freehit', '3xc']

    chips_used = [x['name'] for x in json['chips'] if x['name'] in chip_filter]

    return chips_used

def create_league_chip_dataframe(df):

    manager_ids = df['entry'].to_list()

    rows = []
    for manager_id in manager_ids:
        chips_used = collect_manager_chip_data(manager_id)
        chip_index = [0,0,0]
        n = 0
        for x in ['bboost', 'freehit', '3xc']:
            if x in chips_used:
                chip_index[n] = 1
            else:
                chip_index[n] = 0

            n = n + 1

        chip_index.insert(0, manager_id)
        rows.append(chip_index)

    chip_df = pd.DataFrame(rows, columns=['entry', 'Bench Boost', 'Free Hit', 'Triple Captain'])

    return chip_df

def collect_league_data(league_id):

    url = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings' 

    r = requests.get(url)
    json = r.json()

    league_name = json['league']['name'].replace('/', '_').replace(' ', '_').lower()

    df = pd.DataFrame(json['standings']['results'])

    chip_df = create_league_chip_dataframe(df)

    df = df.join(chip_df, lsuffix='entry', rsuffix='entry')

    df.to_csv(f'data_leagues/{league_name}.csv')
