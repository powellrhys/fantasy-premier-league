# from api_functions import connect_to_database

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import pandas as pd
import warnings
import uvicorn
import pyodbc
import os

from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

# Ignore warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

origins = [
    "http://localhost:5173"
]

# Spin up Fast API application
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def connect_to_database():

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


# Define league data endpoint
@app.get("/api/leagues")
def read_league_data(api_key: str = None):

    # Authenticate request
    if api_key == os.getenv('password'):

        # Collect list of user leages
        cnxn, _ = connect_to_database()
        leagues_df = pd.read_sql('Select * from fpl_league_data', cnxn)

        return JSONResponse(status_code=200, content=leagues_df.to_dict('records'))

    # Raise exception if authentication has failed
    else:
        raise HTTPException(status_code=403, detail="Authentication failed")


# Define player data endpoint
@app.get("/api/players")
def read_player_data(api_key: str = None):

    # Authenticate request
    if api_key == os.getenv('password'):

        # Collect player data
        cnxn, _ = connect_to_database()
        player_data_df = pd.read_sql('Select * from fpl_player_data', cnxn)

        return JSONResponse(status_code=200, content=player_data_df.to_dict('records'))

    # Raise exception if authentication has failed
    else:
        raise HTTPException(status_code=403, detail="Authentication failed")


# Define league table data endpoint
@app.get("/api/league-table")
def read_league_table(api_key: str = None):

    # Authenticate request
    if api_key == os.getenv('password'):

        # Collect league table data
        cnxn, _ = connect_to_database()
        premier_league_table = pd.read_sql('Select * from fpl_premier_league_table', cnxn) \
            .set_index('Position')

        return JSONResponse(status_code=200, content=premier_league_table.to_dict('records'))

    # Raise exception if authentication has failed
    else:
        raise HTTPException(status_code=403, detail="Authentication failed")


# Path to the frontend build directory
frontend_dist_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend-react', 'dist')

# Mount the assets directory to serve static files
app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist_path, 'assets')), name="assets")

# Serve the index.html on the root path
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(frontend_dist_path, "index.html"))

# Serve index.html for all other paths (for React Router support)
@app.get("/{path:path}")
async def serve_any(path: str):
    return FileResponse(os.path.join(frontend_dist_path, "index.html"))


if __name__ == '__main__':

    uvicorn.run(app, host="0.0.0.0", port=8000)
