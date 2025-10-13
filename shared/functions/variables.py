# Import dependencies
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import streamlit as st
import os

class Variables:
    """
    A class to manage environment variables and configuration settings for the app.
    """
    def __init__(self, source: str = "backend") -> None:
        """
        Initialize Variables with environment or Streamlit secrets based on the source.

        Args:
            source (str, optional): Determines where to load configuration from.
                                    "backend" loads from environment variables,
                                    otherwise loads from Streamlit secrets. Defaults to "backend".
        """
        load_dotenv()
        # Shared variables
        if source == "backend":
            self.blob_connection_string = os.getenv('blob_connection_string')
            self.container_name = 'fantasy-premier-league'
            self.blob_service_client = BlobServiceClient.from_connection_string(self.blob_connection_string)
        else:
            self.blob_storage_connection_string = st.secrets["general"]["blob_storage_connection_string"]

        # Fantasy Premier League variables
        league_ids_str = os.getenv("league_ids", "")
        self.league_ids = [int(id) for id in league_ids_str.split(", ")] if league_ids_str else []

        # Privileged Users
        self.privileged_users = [str(id) for id in st.secrets["general"]["privileged_users"].split(", ")]

    def __getitem__(self, key):
        """
        Allow dictionary-style access to environment variable attributes.

        Args: key (str): The attribute name to retrieve.

        Returns: Any: The value of the requested attribute.

        Raises: KeyError: If the requested key does not exist as an attribute.
        """
        # If class as attributes, return items
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"{key} not found in Variables")
