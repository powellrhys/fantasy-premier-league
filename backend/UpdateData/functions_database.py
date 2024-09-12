from dotenv import load_dotenv
import pyodbc
import os

def connect_to_database():

    load_dotenv()

    server = os.getenv('sql_server_name')
    database = os.getenv('sql_server_database')
    username = os.getenv('sql_server_username')
    password = os.getenv('sql_server_password')
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
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
    for _, row in player_df.iterrows():
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


def update_leagues_table(cnxn, cursor, league_df):

    cursor.execute("drop table if exists [dbo].[fpl_league_data]")

    create_table_query = """
        CREATE TABLE fpl_league_data (
            id int,
            event_total int,
            player_name varchar(255),
            league_rank int,
            last_rank int,
            rank_sort int,
            total int,
            entry int,
            entry_name varchar(255),
            bench_boost int,
            free_hit int,
            triple_c int,
            league_name varchar(255),
        );
        """

    cursor.execute(create_table_query)
    cnxn.commit()

    # Insert Dataframe into SQL Server:
    for _, row in league_df.iterrows():
        cursor.execute(f"INSERT INTO fpl_league_data ({','.join(list(league_df.columns))}) "
                       f"values({','.join(['?'] * len(list(league_df.columns)))})",
                       row.id,
                       row.event_total,
                       row.player_name,
                       row.league_rank,
                       row.last_rank,
                       row.rank_sort,
                       row.total,
                       row.entry,
                       row.entry_name,
                       row.bench_boost,
                       row.free_hit,
                       row.triple_c,
                       row.league_name
                       )
    cnxn.commit()


def update_manager_squad_data(cnxn, cursor, manager_squad_df):

    # Drop table if exists
    cursor.execute("drop table if exists [dbo].[fpl_manager_squad_data]")

    # Recreate table in sql database
    create_table_query = """
        CREATE TABLE fpl_manager_squad_data (
            entry int,
            manager_name varchar(255),
            league_name varchar(255),
            player_name varchar(255),
        );
        """

    # Execute create table query
    cursor.execute(create_table_query)
    cnxn.commit()

    # Insert Dataframe into SQL Server:
    for _, row in manager_squad_df.iterrows():
        cursor.execute(f"INSERT INTO fpl_manager_squad_data ({','.join(list(manager_squad_df.columns))}) "
                       f"values({','.join(['?'] * len(list(manager_squad_df.columns)))})",
                       row.entry,
                       row.manager_name,
                       row.league_name,
                       row.player_name,
                       )
    cnxn.commit()


def update_premier_league_table(cnxn, cursor, premier_league_table):

    cursor.execute("drop table if exists [dbo].[fpl_premier_league_table]")

    create_table_query = """
        CREATE TABLE fpl_premier_league_table (
            Position int,
            Team varchar(255),
            Pl int,
            W int,
            D int,
            L int,
            GF int,
            GA int,
            GD int,
            Pts int,
        );
        """

    cursor.execute(create_table_query)
    cnxn.commit()

    # Insert Dataframe into SQL Server:
    for _, row in premier_league_table.iterrows():
        cursor.execute(f"INSERT INTO fpl_premier_league_table ({','.join(list(premier_league_table.columns))}) "
                       f"values({','.join(['?'] * len(list(premier_league_table.columns)))})",
                       row.Position,
                       row.Team,
                       row.Pl,
                       row.W,
                       row.D,
                       row.L,
                       row.GF,
                       row.GA,
                       row.GD,
                       row.Pts,
                       )
    cnxn.commit()
