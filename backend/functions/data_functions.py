from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Import python dependencies
from azure.storage.blob import BlobServiceClient
from typing import Union
from io import StringIO
import pandas as pd
import requests
import os

from functions.data_schemas import (
    player_data_columns
)


class Variables:
    """
    """
    load_dotenv()

    def __init__(self):
        self.blob_connection_string = os.getenv('blob_connection_string')
        self.container_name = 'fantasy-premier-league'
        self.blob_service_client = BlobServiceClient.from_connection_string(self.blob_connection_string)


class BlobStorage:
    """
    A class to handle uploading pandas DataFrames to Azure Blob Storage.
    """

    def upload_dataframe(
            self,
            df: pd.DataFrame,
            file_name: str):
        """
        Upload a pandas DataFrame to blob storage as a CSV.

        Args:
            df (pd.DataFrame): The dataframe to upload.
            blob_path (str): The path within the container (e.g. 'data/fpl.csv').
        """
        vars = Variables()

        # Get a reference to the container
        blob_client = vars.blob_service_client.get_blob_client(container=vars.container_name, blob=file_name)

        # Convert DataFrame to CSV
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Upload the CSV to Blob Storage
        blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)


class FPLApiClient:
    """
    """
    BASE_URL = "https://fantasy.premierleague.com/api"

    def get_json(self, endpoint: str):
        """
        """
        url = f"{self.BASE_URL}/{endpoint}"

        return requests.get(url).json()


class GameWeek:
    """
    """
    @staticmethod
    def get_current() -> Union[int, str]:
        """
        """
        data = FPLApiClient().get_json("bootstrap-static")

        current_gws = [gw["id"] for gw in data["events"] if gw["is_current"]]
        return current_gws[0] if current_gws else 'Outside of Season Window'


class PlayerData:
    """
    """
    def __init__(self):
        """
        """
        self.client = FPLApiClient()

    def get_player_dataframe(self):
        """
        """
        json = self.client.get_json("bootstrap-static")

        # Create dataframe from endpoint components
        elements_df = pd.DataFrame(json['elements'])
        elements_types_df = pd.DataFrame(json['element_types'])
        teams_df = pd.DataFrame(json['teams'])

        # List of variables to store in dataframe
        player_stats_of_interest = player_data_columns

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

        return slim_elements_df.set_index('id')


class Manager:
    def __init__(self, manager_id: int):
        self.manager_id = manager_id

    def get_chip_flags(self) -> dict:
        data = FPLApiClient().get_json(f"entry/{self.manager_id}/history/")
        chips = [chip['name'] for chip in data.get('chips', [])]
        return {
            'entry': self.manager_id,
            'bench_boost': int('bboost' in chips),
            'free_hit': int('freehit' in chips),
            'triple_c': int('3xc' in chips)
        }


class League:
    def __init__(self, league_id: str):
        self.league_id = league_id
        self.client = FPLApiClient()

    def collect_league_data(self) -> pd.DataFrame:
        """
        """
        data = self.client.get_json(f"leagues-classic/{self.league_id}/standings")
        standings_df = pd.DataFrame(data['standings']['results'])

        return standings_df

    def group_league_data(self) -> :


        # # Create chip data
        # chip_data = [Manager(entry['entry'], self.client).get_chip_flags() for entry in data['standings']['results']]
        # chip_df = pd.DataFrame(chip_data)

        # # Merge standings with chip flags
        # full_df = standings_df.merge(chip_df, on='entry', how='left')
        # full_df['league_name'] = data['league']['name']
        # full_df.rename(columns={'rank': 'league_rank'}, inplace=True)

        # return full_df



# def collect_current_gameweek():

#     # Endpoint url
#     url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

#     # Read in data from endpoint
#     r = requests.get(url)
#     gameweeks = r.json()['events']

#     # Collect current gamewek
#     gw = [gw['id'] for gw in gameweeks if gw['is_current']][0]

#     return gw


# def collect_player_data():

#     # Endpoint url
#     url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

#     # Read in data from endpoint
#     r = requests.get(url)
#     json = r.json()

#     # Create dataframe from endpoint components
#     elements_df = pd.DataFrame(json['elements'])
#     elements_types_df = pd.DataFrame(json['element_types'])
#     teams_df = pd.DataFrame(json['teams'])

#     # List of variables to store in dataframe
#     player_stats_of_interest = ['id', 'second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost',
#                                 'minutes', 'transfers_in', 'value_season', 'total_points', 'goals_scored',
#                                 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved',
#                                 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'starts']

#     # Transform dataframe
#     slim_elements_df = elements_df[player_stats_of_interest]
#     slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
#     slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
#     slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
#     slim_elements_df['now_cost'] = slim_elements_df['now_cost'].div(10)

#     # Add position variable to columns needed in final dataframe
#     player_stats_of_interest.append('position')

#     # Filter dataset
#     slim_elements_df = slim_elements_df[player_stats_of_interest]

#     return slim_elements_df


# def collect_manager_chip_data(manager_id):

#     # Endpoint url
#     url = f' https://fantasy.premierleague.com/api/entry/{manager_id}/history/'

#     # Collect endpoint data
#     r = requests.get(url)
#     json = r.json()

#     # List of potential chips
#     chip_filter = ['bboost', 'freehit', '3xc']

#     # Loop through manager data to collect chips used
#     chips_used = [x['name'] for x in json['chips'] if x['name'] in chip_filter]

#     return chips_used


# def create_league_chip_dataframe(df):

#     # Collect list of manager ids
#     manager_ids = df['entry'].to_list()

#     # Loop through managers to find which chips are played
#     rows = []
#     for manager_id in manager_ids:
#         chips_used = collect_manager_chip_data(manager_id)
#         chip_index = [0, 0, 0]
#         n = 0
#         for x in ['bboost', 'freehit', '3xc']:
#             if x in chips_used:
#                 chip_index[n] = 1
#             else:
#                 chip_index[n] = 0
#             n = n + 1

#         chip_index.insert(0, manager_id)
#         rows.append(chip_index)

#     # Create dataframe of manager ids and chips played
#     chip_df = pd.DataFrame(rows, columns=['entry', 'bench_boost', 'free_hit', 'triple_c'])

#     return chip_df


# def collect_single_league_data(league_id):

#     # Endpoint url
#     url = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings'

#     # Collect data from endpoint
#     r = requests.get(url)
#     json = r.json()

#     # Create pandas dataframe of results
#     df = pd.DataFrame(json['standings']['results'])

#     # Create chips used dataframe
#     chip_df = create_league_chip_dataframe(df) \
#         .rename(columns={'entry': 'chip_entry'})

#     # Join league data with chips data
#     df = df.join(chip_df, lsuffix='entry', rsuffix='chip_entry') \
#         .rename(columns={'rank': 'league_rank'}) \
#         .drop(columns=['chip_entry'])
#     df['league_name'] = json['league']['name']

#     return df

# def collect_league_data():
#     league_ids = os.getenv('leagues').replace(' ', '').split(',')

#     league_df = pd.DataFrame(columns=['id', 'event_total', 'player_name', 'league_rank', 'last_rank', 'rank_sort',
#                                       'total', 'entry', 'entry_name', 'bench_boost',
#                                       'free_hit', 'triple_c', 'league_name'])
#     for league_id in league_ids:
#         df = collect_single_league_data(league_id)
#         league_df = pd.concat([league_df, df])

#     return league_df

# def collect_manager_squad_data(cnxn, gameweek):

#     # Define query to extract data from the fpl_leage_data table
#     query = '''
#         select
#             entry,
#             player_name,
#             league_name
#         from
#             fpl_league_data
#     '''

#     # Execute sql query
#     manager_squad_df = pd.read_sql(query, cnxn)

#     # Collect list of unique manager ids
#     unique_managers = list(set(manager_squad_df['entry'].tolist()))

#     # Define empty squad dataframe
#     squad_df = pd.DataFrame(columns=['manager_id', 'squad'])

#     # Iterate through manager ids
#     for manager_id in unique_managers:

#         # Collect squad data for specific manager
#         single_squad_df = collect_single_manager_squad_data(cnxn, manager_id, gameweek)
#         squad_df = pd.concat([squad_df, single_squad_df])

#     # Join squad data to manager data
#     squad_df = squad_df.reset_index().drop(columns=['index'])
#     manager_squad_df = manager_squad_df \
#         .merge(squad_df, left_on='entry', right_on='manager_id', how='left') \
#         .drop(columns=['manager_id']) \
#         .rename(columns={
#             'player_name': 'manager_name',
#             'squad': 'player_name'
#         })

#     return manager_squad_df


# def collect_single_manager_squad_data(cnxn, manager_id, gw):

#     # Define gameweek squad url
#     url = f'https://fantasy.premierleague.com/api/entry/{manager_id}/event/{gw}/picks/'

#     # Collect data from endpoint
#     r = requests.get(url)
#     json = r.json()

#     # Iterate through squad picks - collect player ids
#     pick_ids = [pick['element'] for pick in json['picks']]

#     # Convert ids to player names
#     squad = [collect_player_name_by_id(cnxn, pick_id) for pick_id in pick_ids]

#     # Create squad dataframe
#     squad_df = pd.DataFrame(
#         {'manager_id': [manager_id] * 15,
#          'squad': squad})

#     return squad_df


# def collect_player_name_by_id(cnxn, player_id):

#     # Define query
#     query = f'''
#         select
#             second_name
#         from
#             fpl_player_data
#         where
#             id = {player_id}
#     '''

#     # Collect player name from table
#     player_name = pd.read_sql(query, cnxn).iloc[0]['second_name']

#     return player_name


# def collect_premier_league_table():

#     # Collect html for premier league standings
#     url = 'https://www.bbc.co.uk/sport/football/premier-league/table'
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text)

#     # Collect headers for premier league standings table
#     table1 = soup.find("table", {"class": "ssrcss-14j0ip6-Table e3bga5w5"})
#     headers = []
#     for i in table1.find_all('th'):
#         title = i.text
#         headers.append(title)

#     # Create empty dataframe from headers
#     premier_league_table = pd.DataFrame(columns=headers)

#     # Populate table with values
#     for j in table1.find_all('tr')[1:]:
#         row_data = j.find_all('td')
#         row = [i.text for i in row_data]
#         length = len(premier_league_table)
#         premier_league_table.loc[length] = row

#     # Filter and rename columns in dataframe
#     premier_league_table = premier_league_table[headers[:10]]
#     premier_league_table = premier_league_table.rename(
#         columns={"Played": "Pl",
#                  "Won": "W",
#                  "Drawn": "D",
#                  "Lost": "L",
#                  "Goals For": "GF",
#                  "Goals Against": "GA",
#                  "Goal Difference": "GD",
#                  "Points": "Pts"})

#     # Write table to storage
#     return premier_league_table
