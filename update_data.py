from pages.functions.fixtures import collect_fixture_data
from pages.functions.players import collect_player_data
from pages.functions.league import collect_league_data
from pages.functions.manager import collect_manager_data

from dotenv import load_dotenv
import pandas as pd
import warnings
import os

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

if __name__ == "__main__":
   update_data()