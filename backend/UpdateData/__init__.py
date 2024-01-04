from functions_data_collection import \
    collect_player_data, \
    collect_league_data
from functions_database import \
    connect_to_database, \
    update_player_table, \
    update_leagues_table

import warnings
import logging

# Ignore warnings
warnings.filterwarnings("ignore")

# Configure Logger
logger = logging.getLogger('BASIC')

# Connect to Database
cnxn, cursor = connect_to_database()
logger.info('Connected to Database')

# Collect and Update Player Data
player_df = collect_player_data()
update_player_table(cnxn, cursor, player_df)
logger.info('Player Data updated in SQL')

# Collect and Update League Data
league_df = collect_league_data()
update_leagues_table(cnxn, cursor, league_df)
logger.info('League Data updated in SQL')

# Close SQL database connection
cursor.close()
