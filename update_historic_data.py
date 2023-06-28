from pages.functions.support_functions import \
    read_csv

from dotenv import load_dotenv
import pandas as pd
import os


def update_week_by_week_player_data(season):

   big_df = pd.DataFrame()
   players = os.listdir('data_all_players')
   for file in players:
      df = read_csv(f'data_all_players/{file}')
      df['name'] = file.replace('.csv', '')
      df['season_x'] = season
      
      big_df = pd.concat([big_df, df])

   big_df.to_csv(f'data_historic/static/player_data_{season}.csv')

if __name__ == "__main__":

   # Load env variables
   load_dotenv()
   season = os.getenv('season')

   # Create current season breakdown table
   update_week_by_week_player_data(season)