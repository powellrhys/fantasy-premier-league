# Import python dependencies
import warnings
import logging

# Import project dependencies
from functions.data_functions import (
    BlobStorage,
    PlayerData,
    GameWeek,
    Manager,
    League
)

# Ignore warnings
warnings.filterwarnings("ignore")

# Configure Logger
logger = logging.getLogger('BASIC')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
log_handler = logging.StreamHandler()
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

# logger.info('Determining current Game Week...')
# gw = GameWeek().get_current()
# logger.info(f'Current Game Week: {gw} \n')

# logger.info('Collecting player data...')
# player_df = PlayerData().get_player_dataframe()
# logger.info(f'Data collected for {len(player_df)} players \n')

# logger.info('Writing player data to blob storage...')
# BlobStorage().upload_dataframe(df=player_df, file_name='player_data.csv')
# logger.info('Player data written to blob storage \n')

# x = Manager(manager_id=1849308).get_chip_flags()
# print(x)

y = League(league_id=332093).collect_data()

# # Connect to Database
# logger.info('Connecting to Database...')
# cnxn, cursor = connect_to_database()
# logger.info('Connected to Database')

# # Collect and Update Player Data
# logger.info('Updating Player Data in SQL...')
# player_df = collect_player_data()
# update_player_table(cnxn, cursor, player_df)
# logger.info('Player Data updated in SQL')

# # Collect and Update League Data
# logger.info('Updating League Data in SQL...')
# league_df = collect_league_data()
# update_leagues_table(cnxn, cursor, league_df)
# logger.info('League Data updated in SQL')

# logger.info('Updating Manager Squad Data in SQL...')
# gameweek = collect_current_gameweek()
# manager_squad_df = collect_manager_squad_data(cnxn, gameweek)
# update_manager_squad_data(cnxn, cursor, manager_squad_df)
# logger.info('Manager Squad Data updated in SQL')

# # Collect and Update Premier League Table Data
# logger.info('Updating Premier League Table Data in SQL...')
# premier_league_table = collect_premier_league_table()
# update_premier_league_table(cnxn, cursor, premier_league_table)
# logger.info('Premier League Table Data Updated in SQL')

# # Close SQL database connection
# cursor.close()
