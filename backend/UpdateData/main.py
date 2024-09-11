from functions_data_collection import \
    collect_player_data, \
    collect_league_data, \
    collect_premier_league_table, \
    collect_manager_squad_data
from functions_database import \
    connect_to_database, \
    update_player_table, \
    update_leagues_table, \
    update_premier_league_table, \
    update_manager_squad_data

import warnings
import logging

# Ignore warnings
warnings.filterwarnings("ignore")

# Configure Logger
logger = logging.getLogger('BASIC')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
log_handler = logging.StreamHandler()
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

# Connect to Database
logger.info('Connecting to Database...')
cnxn, cursor = connect_to_database()
logger.info('Connected to Database')

# Collect and Update Player Data
logger.info('Updating Player Data in SQL...')
player_df = collect_player_data()
update_player_table(cnxn, cursor, player_df)
logger.info('Player Data updated in SQL')

# Collect and Update League Data
logger.info('Updating League Data in SQL...')
league_df = collect_league_data()
update_leagues_table(cnxn, cursor, league_df)
logger.info('League Data updated in SQL')

logger.info('Updating Manager Squad Data in SQL...')
manager_squad_df = collect_manager_squad_data(cnxn, cursor)
update_manager_squad_data(cnxn, cursor, manager_squad_df)
logger.info('Manager Squad Data updated in SQL')

# Collect and Update Premier League Table Data
logger.info('Updating Premier League Table Data in SQL...')
premier_league_table = collect_premier_league_table()
update_premier_league_table(cnxn, cursor, premier_league_table)
logger.info('Premier League Table Data Updated in SQL')

# Close SQL database connection
cursor.close()
