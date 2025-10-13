# Import dependencies
from .fpl_api_client import FPLApiClient
from typing import Union

class GameWeek:
    """
    A class to get information about the current Fantasy Premier League game week.
    """
    @staticmethod
    def get_current() -> Union[int, str]:
        """
        Return the current gameweek ID, or a message if outside the season window.
        """
        # Collect data
        data = FPLApiClient().get_json("bootstrap-static")

        # Collect game weeks from data
        current_gws = [gw["id"] for gw in data["events"] if gw["is_current"]]

        # Return current game week
        return current_gws[0] if current_gws else 'Outside of Season Window'
