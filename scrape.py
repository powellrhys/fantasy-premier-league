from data_scraping.fixtures import collect_fixture_data
from data_scraping.players import collect_player_data

import warnings

warnings.filterwarnings("ignore")

collect_fixture_data()
collect_player_data()