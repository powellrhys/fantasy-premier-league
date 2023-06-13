from data_scraping.fixtures import collect_fixture_data
from data_scraping.players import collect_player_data
from data_scraping.league import collect_league_data

import warnings
import os

warnings.filterwarnings("ignore")

from dotenv import load_dotenv

load_dotenv()

league_ids = os.getenv('leagues').replace(' ', '').split(',')

collect_fixture_data()
collect_player_data()

for league_id in league_ids:
    collect_league_data(league_id)