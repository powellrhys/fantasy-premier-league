# Import dependencies
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import streamlit as st
import os

class Variables:
    """
    """
    load_dotenv()

    def __init__(self, source: str = "backend") -> None:
        """
        """
        # Shared variables
        if source == "backend":
            self.blob_connection_string = os.getenv('blob_connection_string')
            self.container_name = 'fantasy-premier-league'
            self.blob_service_client = BlobServiceClient.from_connection_string(self.blob_connection_string)
        else:
            self.blob_storage_connection_string = st.secrets["general"]["blob_storage_connection_string"]

        # Fantasy Premier League variables
        self.league_ids = [int(id) for id in os.getenv(key="league_ids", default=[]).split(", ")]

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
