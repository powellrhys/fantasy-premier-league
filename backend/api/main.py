from api_functions import connect_to_database

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import pandas as pd
import warnings
import uvicorn
import os

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
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define Root Endpoint
@app.get("/")
async def read_root():
    content = {"message": "Fantasy Premier League Fast API Application"}
    return JSONResponse(status_code=200, content=content)


# Define league data endpoint
@app.get("/leagues")
def read_league_data(api_key: str = None):

    # Authenticate request
    if api_key == os.getenv('password'):

        # Collect list of user leages
        cnxn, _ = connect_to_database()
        leagues_df = pd.read_sql('Select * from fpl_league_data', cnxn)

        return JSONResponse(status_code=200, content=leagues_df.to_dict())

    # Raise exception if authentication has failed
    else:
        raise HTTPException(status_code=403, detail="Authentication failed")


# Define player data endpoint
@app.get("/players")
def read_player_data(api_key: str = None):

    # Authenticate request
    if api_key == os.getenv('password'):

        # Collect player data
        cnxn, _ = connect_to_database()
        player_data_df = pd.read_sql('Select * from fpl_player_data', cnxn)

        return JSONResponse(status_code=200, content=player_data_df.to_dict())

    # Raise exception if authentication has failed
    else:
        raise HTTPException(status_code=403, detail="Authentication failed")


# Define league table data endpoint
@app.get("/league-table")
def read_league_table(api_key: str = None):

    # Authenticate request
    if api_key == os.getenv('password'):

        # Collect league table data
        cnxn, _ = connect_to_database()
        premier_league_table = pd.read_sql('Select * from fpl_premier_league_table', cnxn) \
            .set_index('Position')

        return JSONResponse(status_code=200, content=premier_league_table.to_dict())

    # Raise exception if authentication has failed
    else:
        raise HTTPException(status_code=403, detail="Authentication failed")


if __name__ == '__main__':

    uvicorn.run(app, host="0.0.0.0", port=8000)
