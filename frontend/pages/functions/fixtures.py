import pandas as pd
import requests

def collect_fixture_data():

    # Set endpoints urls
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/' 
    fix_url = 'https://fantasy.premierleague.com/api/fixtures/?future=0'

    # Read data from first endpoint
    r = requests.get(url)
    json = r.json()

    # Create teams dataframe
    teams_df = pd.DataFrame(json['teams'])

    # Collect data from second endpoint
    fix_r = requests.get(fix_url)
    json = fix_r.json()

    # Create fixtures dataframe
    fixtures = pd.DataFrame(json)

    # Filter data
    fixtures_slim = fixtures[['team_h', 'team_a','team_h_difficulty', 'team_a_difficulty','event']]
    fixtures_slim['team_a'] = fixtures_slim.team_a.map(teams_df.set_index('id').name)
    fixtures_slim['team_h'] = fixtures_slim.team_h.map(teams_df.set_index('id').name)

    # Further filtering and rename of columns
    fixtures_stacked1 = fixtures_slim[['event','team_h','team_h_difficulty']]
    fixtures_stacked1.rename(columns={"event": "GW", "team_h": "Team", "team_h_difficulty": "Diff"}, inplace=True)
    fixtures_stacked2 = fixtures_slim[['event','team_a','team_a_difficulty']]
    fixtures_stacked2.rename(columns={"event": "GW", "team_a": "Team", "team_a_difficulty": "Diff"}, inplace=True)
    fixtures_stacked = pd.concat([fixtures_stacked1, fixtures_stacked2]).sort_values('GW').reset_index(drop=True)

    # Write fixture data to storage
    fixtures_stacked.to_csv('data/fixtures.csv')
