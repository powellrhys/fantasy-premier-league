import warnings
from functions_data_collection import collect_player_data
from functions_database import connect_to_database, update_player_table

# Ignore warnings
warnings.filterwarnings("ignore")
player_df = collect_player_data()
cnxn, cursor = connect_to_database()
update_player_table(cnxn, cursor, player_df)
