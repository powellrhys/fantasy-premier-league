from pages.functions.support_functions import \
    read_csv

from dotenv import load_dotenv
import warnings
import pandas as pd
import os


def update_week_by_week_player_data(season):

   # Create empty dataframe
   big_df = pd.DataFrame()

   # Loop through player data - append to big dataframe
   players = os.listdir('data_all_players')
   for file in players:
      df = read_csv(f'data_all_players/{file}')
      df['name'] = file.replace('.csv', '')
      df['season_x'] = season
      
      big_df = pd.concat([big_df, df])

   # Write complete dataframe to local storage
   big_df.to_csv(f'data_historic/static/player_data_{season}.csv')

def create_season_view(df):

   # Group data by season 
   season_df = df.groupby(['season_x']).sum()

   # Filter dataframe by columns
   columns = ['goals_scored', 'assists', 'own_goals', 'penalties_missed', 'penalties_saved', 
              'yellow_cards', 'red_cards', 'total_points']
   season_df = season_df[columns]

   # Write dataframe to local storage
   season_df.to_csv('data_historic/views/season_breakdown.csv')

def create_all_time_player_performance_view(df):
   
   # Group dataframe by season, name and position
   player_df = df.groupby(['season_x', 'name', 'position']).sum().sort_values(by='total_points', ascending=False)

   # Filter dataframe by columns
   columns = ['goals_scored', 'assists', 'own_goals', 'penalties_missed', 'penalties_saved', 
              'clean_sheets', 'minutes', 'yellow_cards', 'red_cards', 'value', 'total_points']
   player_df = player_df[columns]

   # Write dataframe to local stroage
   player_df.to_csv('data_historic/views/all_time_player_performance.csv')

   return player_df

def create_seasonal_position_view(df):
   
   # Group data by season and position
   player_df = df.groupby(['season_x', 'position']).sum()

   # Filter dataframe by columns
   columns = ['goals_scored', 'assists', 'own_goals', 'penalties_missed', 'penalties_saved', 
              'clean_sheets', 'minutes', 'yellow_cards', 'red_cards', 'value', 'total_points']
   player_df = player_df[columns]

   # Write data to local storage
   player_df.to_csv('data_historic/views/seasonal_position.csv')

if __name__ == "__main__":

   # Ignore warnings
   warnings.filterwarnings("ignore")

   # Load env variables
   load_dotenv()
   season = os.getenv('season')

   # Create current season breakdown table
   update_week_by_week_player_data(season)

   # Collect and write views to local storage
   df = pd.read_csv('data_historic/static/historic_player_data.csv', dtype={"team_x": str}).drop('index', axis=1)
   create_all_time_player_performance_view(df)
   create_season_view(df)
   create_seasonal_position_view(df)
