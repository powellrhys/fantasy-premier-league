from pages.functions.support_functions import \
    read_csv

from dotenv import load_dotenv
import warnings
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

def create_season_view(df):
   season_df = df.groupby(['season_x']).sum()

   columns = ['goals_scored', 'assists', 'own_goals', 'penalties_missed', 'penalties_saved', 
              'yellow_cards', 'red_cards', 'total_points']
   
   season_df = season_df[columns]

   season_df.to_csv('data_historic/views/season_breakdown.csv')

def create_all_time_player_performance_view(df):
   
   player_df = df.groupby(['season_x', 'name', 'position']).sum().sort_values(by='total_points', ascending=False)

   columns = ['goals_scored', 'assists', 'own_goals', 'penalties_missed', 'penalties_saved', 
              'clean_sheets', 'minutes', 'yellow_cards', 'red_cards', 'value', 'total_points']
   
   player_df = player_df[columns]

   player_df.to_csv('data_historic/views/all_time_player_performance.csv')

   return player_df

def create_seasonal_position_view(df):
   
   player_df = df.groupby(['season_x', 'position']).sum().sort_values(by='total_points', ascending=False)

   columns = ['goals_scored', 'assists', 'own_goals', 'penalties_missed', 'penalties_saved', 
              'clean_sheets', 'minutes', 'yellow_cards', 'red_cards', 'value', 'total_points']
   
   player_df = player_df[columns]

   player_df.to_csv('data_historic/views/seasonal_position.csv')

if __name__ == "__main__":

   # Ignore warnings
   warnings.filterwarnings("ignore")

   # Load env variables
   load_dotenv()
   season = os.getenv('season')

   # Create current season breakdown table
   update_week_by_week_player_data(season)

   df = pd.read_csv('data_historic/static/historic_player_data.csv', dtype={"team_x": str}).drop('index', axis=1)
   create_all_time_player_performance_view(df)
   create_season_view(df)
   create_seasonal_position_view(df)
