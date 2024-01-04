import requests
import pandas as pd

def collect_manager_chip_data(manager_id):

    # Endpoint url
    url = f' https://fantasy.premierleague.com/api/entry/{manager_id}/history/'

    # Collect endpoint data 
    r = requests.get(url)
    json = r.json()

    # List of potential chips
    chip_filter = ['bboost', 'freehit', '3xc']

    # Loop through manager data to collect chips used
    chips_used = [x['name'] for x in json['chips'] if x['name'] in chip_filter]

    return chips_used

def create_league_chip_dataframe(df):

    # Collect list of manager ids
    manager_ids = df['entry'].to_list()

    # Loop through managers to find which chips are played
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

    # Create dataframe of manager ids and chips played
    chip_df = pd.DataFrame(rows, columns=['entry', 'Bench Boost', 'Free Hit', 'Triple Captain'])

    return chip_df

def collect_league_data(league_id):

    # Endpoint url
    url = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings' 

    # Collect data from endpoint
    r = requests.get(url)
    json = r.json()

    # Collect league name
    league_name = json['league']['name'].replace('/', '_').replace(' ', '_').lower()

    # Create pandas dataframe of results
    df = pd.DataFrame(json['standings']['results'])

    # Create chips used dataframe
    chip_df = create_league_chip_dataframe(df)

    # Join league data with chips data
    df = df.join(chip_df, lsuffix='entry', rsuffix='entry')

    # Write data to storage
    df.to_csv(f'data_leagues/{league_name}.csv')

    return json['league']['name']
