# Import dependencies
import requests

class FPLApiClient:
    """
    A simple client to get data from the Fantasy Premier League API.
    """
    # Define base url
    BASE_URL = "https://fantasy.premierleague.com/api"

    def get_json(self, endpoint: str):
        """
        Get JSON data from the given API endpoint.
        """
        # Define url
        url = f"{self.BASE_URL}/{endpoint}"

        return requests.get(url).json()
