from scraping_functions.fixtures import collect_fixture_data
from scraping_functions.players import collect_player_data
from scraping_functions.league import collect_league_data

from dotenv import load_dotenv
import warnings
import os

warnings.filterwarnings("ignore")
load_dotenv()

collect_fixture_data()
collect_player_data()

league_ids = os.getenv('leagues').replace(' ', '').split(',')

for league_id in league_ids:
    collect_league_data(league_id)