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

   # Create my player directory if not already created
   if not os.path.exists('data_my_players'):
      os.makedirs('data_my_players')

   # Remove current data from directory 
   current_file_names = os.listdir('data_my_players')
   for file in current_file_names:
      os.remove(f'data_my_players/{file}')

   # Read in player and current team data
   player_data_df = read_csv('data/players.csv')
   
   if not os.path.exists('data/my_team.csv'):
      player_data_df = read_csv('data/players.csv')

      # Generate player name lists based on position 
      gk1 = player_data_df[player_data_df['position'] == 'Goalkeeper']['second_name'].to_list()[0]
      def1 = player_data_df[player_data_df['position'] == 'Defender']['second_name'].to_list()[0]
      mid1 = player_data_df[player_data_df['position'] == 'Midfielder']['second_name'].to_list()[0]
      fow1 = player_data_df[player_data_df['position'] == 'Forward']['second_name'].to_list()[0]

      my_team_data = [gk1, gk1, def1, def1, def1, def1, def1, mid1, 
                      mid1, mid1, mid1, mid1, fow1, fow1, fow1]
      
      df = pd.DataFrame(data=my_team_data, columns=['0'])

      df.to_csv('data/my_team.csv')

   current_team = read_csv('data/my_team.csv')['0'].to_list()

   # Collect player data for players in current team
   for player_name in current_team:
      player_id = player_data_df[player_data_df['second_name'] == player_name]['id'].to_list()[0]
      collect_unique_player_data(player_id, player_name, 'data_my_players')

def update_data():

   # Ignore warnings
   warnings.filterwarnings("ignore")

   # Load env variables
   load_dotenv()

   # Create data directory if not already created
   if not os.path.exists('data'):
      os.makedirs('data')

   # Create data leagues directory if not already created
   if not os.path.exists('data_leagues'):
      os.makedirs('data_leagues')

   # Collect fixture and player data
   collect_fixture_data()
   collect_player_data()

   # Collect manager data
   manager_id = os.getenv('manager_id')
   collect_manager_data(manager_id)

   # Collect FPL league data
   league_ids = os.getenv('leagues').replace(' ', '').split(',')
   leagues = []
   for league_id in league_ids:
      league_name = collect_league_data(league_id)

      # Create series of league ids
      leagues.append(league_name)
      leagues_df = pd.Series(leagues)

      # Write league data to storage
      leagues_df.to_csv('data_leagues/list_of_leagues.csv')

def update_all_player_data():
   
   # Create all player directory if not already created
   if not os.path.exists('data_all_players'):
      os.makedirs('data_all_players')

   # Collect general player data
   player_data_df = read_csv('data/players.csv')
   all_player_names = player_data_df['second_name'].to_list()

   # Collect in depth player data for all players
   for player_name in all_player_names:
      player_id = player_data_df[player_data_df['second_name'] == player_name]['id'].to_list()[0]
      collect_unique_player_data(player_id, player_name, 'data_all_players')

def update_premier_league_table():

   # Collect html for premier league standings
   url = 'https://www.bbc.co.uk/sport/football/premier-league/table'
   page = requests.get(url)
   soup = BeautifulSoup(page.text)

   # Collect headers for premier league standings table
   table1 = soup.find("table",{"class":"ssrcss-14j0ip6-Table e3bga5w5"})
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
               "Points" : "Pts"})

   # Write table to storage
   premier_league_table.to_csv('data/premier_league_table.csv')

if __name__ == "__main__":
   update_data()
   update_my_team_data()
   update_premier_league_table()
   # update_all_player_data()
