from pages.functions.fixtures import collect_fixture_data
from pages.functions.players import collect_player_data
from pages.functions.league import collect_league_data
from pages.functions.manager import collect_manager_data

from dotenv import load_dotenv
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
   for league_id in league_ids:
      collect_league_data(league_id)

if __name__ == "__main__":
   update_data()