from dotenv import load_dotenv
from fastapi import FastAPI
import pandas as pd
import uvicorn
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


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the model API!"}


@app.get("/leagues")
def read_league_data():

    # Collect list of user leages
    cnxn, _ = connect_to_database()
    leagues_df = pd.read_sql('Select * from fpl_league_data', cnxn)

    return leagues_df.to_dict()


@app.get("/players")
def read_player_data():

    # Collect player data
    cnxn, _ = connect_to_database()
    player_data_df = pd.read_sql('Select * from fpl_player_data', cnxn)

    return player_data_df.to_dict()


@app.get("/league-table")
def read_league_table():

    # Collect league table data
    cnxn, _ = connect_to_database()
    premier_league_table = pd.read_sql('Select * from fpl_premier_league_table', cnxn) \
        .set_index('Position')

    return premier_league_table.to_dict()


if __name__ == '__main__':

    uvicorn.run(app, host="0.0.0.0", port=8000)
