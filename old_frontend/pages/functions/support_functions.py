import pandas as pd

def read_csv(path):

    # Read csv data path specified
    df = pd.read_csv(path, index_col=False)

    return df

def summarise_manager_data(path):

    # Read in manager data
    df = read_csv(path)
    df.columns = ['Key', 'Value']

    # Collect manager data
    team_name = df.loc[df['Key'] == 'name', 'Value'].values[0]
    region = df.loc[df['Key'] == 'player_region_name', 'Value'].values[0]
    gameweek_points = df.loc[df['Key'] == 'summary_event_points', 'Value'].values[0]
    overall_points = df.loc[df['Key'] == 'summary_overall_points', 'Value'].values[0]
    overall_rank = df.loc[df['Key'] == 'summary_overall_rank', 'Value'].values[0]

    return team_name, region, gameweek_points, overall_points, overall_rank

def find_player_index_in_list(current_team, gk_names, def_names, mid_names, fow_names):

    # Loop through 15 picks, finding player ID
    index = []
    for i in range(15):
        if i <= 1:
            player_index = gk_names.index(current_team[i])
        elif i <= 6:
            player_index = def_names.index(current_team[i])
        elif i <= 11:
            player_index = mid_names.index(current_team[i])
        else:
            player_index = fow_names.index(current_team[i])
        index.append(player_index)

    return index
