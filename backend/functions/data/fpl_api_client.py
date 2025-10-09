# Import dependencies
import requests

class FPLApiClient:
    """
    """
    BASE_URL = "https://fantasy.premierleague.com/api"

    def get_json(self, endpoint: str):
        """
        """
        url = f"{self.BASE_URL}/{endpoint}"

        return requests.get(url).json()
