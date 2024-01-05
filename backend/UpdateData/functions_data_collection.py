from dotenv import load_dotenv
from bs4 import BeautifulSoup

import pandas as pd
import requests
import os

load_dotenv()

def collect_player_data():

    # Endpoint url
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    # Read in data from endpoint
    r = requests.get(url)
    json = r.json()

    # Create dataframe from endpoint components
    elements_df = pd.DataFrame(json['elements'])
    elements_types_df = pd.DataFrame(json['element_types'])
    teams_df = pd.DataFrame(json['teams'])

    # List of variables to store in dataframe
    player_stats_of_interest = ['id', 'second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost',
                                'minutes', 'transfers_in', 'value_season', 'total_points', 'goals_scored',
                                'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved',
                                'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'starts']

    # Transform dataframe
    slim_elements_df = elements_df[player_stats_of_interest]
    slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
    slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
    slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
    slim_elements_df['now_cost'] = slim_elements_df['now_cost'].div(10)

    # Add position variable to columns needed in final dataframe
    player_stats_of_interest.append('position')

    # Filter dataset
    slim_elements_df = slim_elements_df[player_stats_of_interest]

    return slim_elements_df


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
        chip_index = [0, 0, 0]
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
    chip_df = pd.DataFrame(rows, columns=['entry', 'bench_boost', 'free_hit', 'triple_c'])

    return chip_df


def collect_single_league_data(league_id):

    # Endpoint url
    url = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings'

    # Collect data from endpoint
    r = requests.get(url)
    json = r.json()

    # Create pandas dataframe of results
    df = pd.DataFrame(json['standings']['results'])

    # Create chips used dataframe
    chip_df = create_league_chip_dataframe(df)

    # Join league data with chips data
    df = df.join(chip_df, lsuffix='entry', rsuffix='entry') \
        .drop(columns=['entryentry'], axis=1) \
        .rename(columns={'rank': 'league_rank'})
    df['league_name'] = json['league']['name']

    return df

def collect_league_data():
    league_ids = os.getenv('leagues').replace(' ', '').split(',')

    league_df = pd.DataFrame(columns=['id', 'event_total', 'player_name', 'league_rank', 'last_rank', 'rank_sort',
                                      'total', 'entry_name', 'bench_boost',
                                      'free_hit', 'triple_c', 'league_name'])
    for league_id in league_ids:
        df = collect_single_league_data(league_id)
        league_df = pd.concat([league_df, df])

    return league_df

def collect_premier_league_table():

    # Collect html for premier league standings
    url = 'https://www.bbc.co.uk/sport/football/premier-league/table'
    page = requests.get(url)
    soup = BeautifulSoup(page.text)

    # Collect headers for premier league standings table
    table1 = soup.find("table", {"class": "ssrcss-14j0ip6-Table e3bga5w5"})
    headers = []
    for i in table1.find_all('th'):
        title = i.text
        headers.append(title)

    # Create empty dataframe from headers
    premier_league_table = pd.DataFrame(columns=headers)

    # Populate table with values
    for j in table1.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(premier_league_table)
        premier_league_table.loc[length] = row

    # Filter and rename columns in dataframe
    premier_league_table = premier_league_table[headers[:10]]
    premier_league_table = premier_league_table.rename(
        columns={"Played": "Pl",
                 "Won": "W",
                 "Drawn": "D",
                 "Lost": "L",
                 "Goals For": "GF",
                 "Goals Against": "GA",
                 "Goal Difference": "GD",
                 "Points": "Pts"})

    # Write table to storage
    return premier_league_table
