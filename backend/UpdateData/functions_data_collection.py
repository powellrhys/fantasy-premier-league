import requests
import pandas as pd


def collect_player_data():

    # Endpoint url
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    # Read in data from endpoint
    r = requests.get(url)
    json = r.json()

    # Create dataframe from endpoint components
    elements_df = pd.DataFrame(json['elements'])
    elements_types_df = pd.DataFrame(json['element_types'])
    teams_df = pd.DataFrame(json['teams'])

    # List of variables to store in dataframe
    player_stats_of_interest = ['id', 'second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost',
                                'minutes', 'transfers_in', 'value_season', 'total_points', 'goals_scored',
                                'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved',
                                'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'starts']

    # Transform dataframe
    slim_elements_df = elements_df[player_stats_of_interest]
    slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
    slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
    slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
    slim_elements_df['now_cost'] = slim_elements_df['now_cost'].div(10)

    # Add position variable to columns needed in final dataframe
    player_stats_of_interest.append('position')

    # Filter dataset
    slim_elements_df = slim_elements_df[player_stats_of_interest]

    return slim_elements_df
