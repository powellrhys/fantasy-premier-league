# Import dependencies
from .functions.orchestration import FPLScrapper

# Run workflow
FPLScrapper().run()

# # Import dependencies
# from backend.functions.logging import configure_logging
# from backend.functions.data import GameWeek, PlayerData, Manager, League
# from shared.functions import BlobStorage
# import pandas as pd

# # # Configure Logger
# logger = configure_logging()

# # logger.info('Determining current Game Week...')
# # gw = GameWeek().get_current()
# # logger.info(f'Current Game Week: {gw} \n')

# # logger.info('Collecting player data...')
# # player_df = PlayerData().get_player_dataframe()
# # logger.info(f'Data collected for {len(player_df)} players \n')

# # logger.info('Writing player data to blob storage...')
# # BlobStorage().upload_dataframe(df=player_df, file_name='player_data.csv')
# # logger.info('Player data written to blob storage \n')

# league_ids = [268236, 532770, 1419521, 2269311]

# all_league_df = pd.DataFrame()
# for league_id in league_ids:

#     logger.info("Collecting managerial league data...")
#     league_df = League(league_id=league_id).collect_league_data()
#     logger.info("Managerial league data collected \n")

#     all_league_df = pd.concat([all_league_df, league_df], ignore_index=True)

#     logger.info('Writing player data to blob storage...')
#     BlobStorage().upload_dataframe(df=league_df, file_name='league_df.csv')
#     logger.info('Player data written to blob storage \n')

# # # Connect to Database
# # logger.info('Connecting to Database...')
# # cnxn, cursor = connect_to_database()
# # logger.info('Connected to Database')

# # # Collect and Update Player Data
# # logger.info('Updating Player Data in SQL...')
# # player_df = collect_player_data()
# # update_player_table(cnxn, cursor, player_df)
# # logger.info('Player Data updated in SQL')

# # # Collect and Update League Data
# # logger.info('Updating League Data in SQL...')
# # league_df = collect_league_data()
# # update_leagues_table(cnxn, cursor, league_df)
# # logger.info('League Data updated in SQL')

# # logger.info('Updating Manager Squad Data in SQL...')
# # gameweek = collect_current_gameweek()
# # manager_squad_df = collect_manager_squad_data(cnxn, gameweek)
# # update_manager_squad_data(cnxn, cursor, manager_squad_df)
# # logger.info('Manager Squad Data updated in SQL')

# # # Collect and Update Premier League Table Data
# # logger.info('Updating Premier League Table Data in SQL...')
# # premier_league_table = collect_premier_league_table()
# # update_premier_league_table(cnxn, cursor, premier_league_table)
# # logger.info('Premier League Table Data Updated in SQL')

# # # Close SQL database connection
# # cursor.close()
