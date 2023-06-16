from pages.functions.support_functions import \
   read_csv
from pages.functions.fixtures import \
   collect_fixture_data
from pages.functions.players import \
   collect_player_data, \
   collect_unique_player_data
from pages.functions.manager import \
   collect_manager_data
from pages.functions.league import \
   collect_league_data

from dotenv import load_dotenv
from bs4 import BeautifulSoup

import pandas as pd
import warnings
import requests
import os

def update_my_team_data():

   if not os.path.exists('data_my_players'):
      os.makedirs('data_my_players')

   current_file_names = os.listdir('data_my_players')
   for file in current_file_names:
      os.remove(f'data_my_players/{file}')

   player_data_df = read_csv('data/players.csv')
   current_team = read_csv('data/my_team.csv')['0'].to_list()

   for player_name in current_team:
      player_id = player_data_df[player_data_df['second_name'] == player_name]['id'].to_list()[0]
      collect_unique_player_data(player_id, player_name, 'data_my_players')

def update_data():

   warnings.filterwarnings("ignore")
   load_dotenv()

   if not os.path.exists('data'):
      os.makedirs('data')

   if not os.path.exists('data_leagues'):
      os.makedirs('data_leagues')

   collect_fixture_data()
   collect_player_data()

   manager_id = os.getenv('manager_id')
   collect_manager_data(manager_id)

   league_ids = os.getenv('leagues').replace(' ', '').split(',')
   leagues = []
   for league_id in league_ids:
      league_name = collect_league_data(league_id)

      leagues.append(league_name)
      leagues_df = pd.Series(leagues)

      leagues_df.to_csv('data_leagues/list_of_leagues.csv')

def update_all_player_data():
   
   if not os.path.exists('data_all_players'):
      os.makedirs('data_all_players')

   player_data_df = read_csv('data/players.csv')
   all_player_names = player_data_df['second_name'].to_list()

   for player_name in all_player_names:
      player_id = player_data_df[player_data_df['second_name'] == player_name]['id'].to_list()[0]
      collect_unique_player_data(player_id, player_name, 'data_all_players')

def update_premier_league_table():

   url = 'https://www.bbc.co.uk/sport/football/premier-league/table'
   page = requests.get(url)
   soup = BeautifulSoup(page.text)

   table1 = soup.find("table",{"class":"ssrcss-14j0ip6-Table e3bga5w5"})
   headers = []
   for i in table1.find_all('th'):
      title = i.text
      headers.append(title)

   premier_league_table = pd.DataFrame(columns=headers)

   for j in table1.find_all('tr')[1:]:
      row_data = j.find_all('td')
      row = [i.text for i in row_data]
      length = len(premier_league_table)
      premier_league_table.loc[length] = row

   premier_league_table = premier_league_table[headers[:10]]
   premier_league_table = premier_league_table.rename(
      columns={"Played": "Pl",
               "Won": "W",
               "Drawn": "D",
               "Lost": "L",
               "Goals For": "GF",
               "Goals Against": "GA",
               "Goal Difference": "GD",
               "Points" : "Pts"})

   premier_league_table.to_csv('data/premier_league_table.csv')

if __name__ == "__main__":
   update_premier_league_table()
   # update_data()
   # update_my_team_data()
   # update_all_player_data()
