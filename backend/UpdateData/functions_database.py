from dotenv import load_dotenv
import pyodbc
import os

def connect_to_database():

    load_dotenv()

    server = os.getenv('sql_server_name')
    database = os.getenv('sql_serve_database')
    username = os.getenv('sql_server_username')
    password = os.getenv('sql_server_password')
    cnxn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=' + server + ';'
                          'DATABASE=' + database + ';'
                          'UID=' + username + ';'
                          'PWD=' + password)
    cursor = cnxn.cursor()

    return cnxn, cursor

def update_player_table(cnxn, cursor, player_df):

    cursor.execute("drop table if exists [dbo].[fpl_player_data]")

    create_table_query = """
        CREATE TABLE fpl_player_data (
            id int,
            second_name varchar(255),
            team varchar(255),
            element_type int,
            selected_by_percent decimal(12,2),
            now_cost decimal(12,2),
            minutes int,
            transfers_in int,
            value_season decimal(12,2),
            total_points int,
            goals_scored int,
            assists int,
            clean_sheets int,
            goals_conceded int,
            own_goals int,
            penalties_saved int,
            penalties_missed int,
            yellow_cards int,
            red_cards int,
            saves int,
            starts int,
            position varchar(255)
        );
        """

    cursor.execute(create_table_query)
    cnxn.commit()

    # Insert Dataframe into SQL Server:
    for index, row in player_df.iterrows():
        cursor.execute(f"INSERT INTO fpl_player_data ({','.join(list(player_df.columns))}) "
                       f"values({','.join(['?'] * len(list(player_df.columns)))})",
                       row.id,
                       row.second_name,
                       row.team,
                       row.element_type,
                       row.selected_by_percent,
                       row.now_cost,
                       row.minutes,
                       row.transfers_in,
                       row.value_season,
                       row.total_points,
                       row.goals_scored,
                       row.assists,
                       row.clean_sheets,
                       row.goals_conceded,
                       row.own_goals,
                       row.penalties_saved,
                       row.penalties_missed,
                       row.yellow_cards,
                       row.red_cards,
                       row.saves,
                       row.starts,
                       row.position
                       )
    cnxn.commit()
    cursor.close()
