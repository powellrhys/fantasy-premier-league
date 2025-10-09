# Import dependencies
from .fpl_api_client import FPLApiClient
from typing import Union

class GameWeek:
    """
    """
    @staticmethod
    def get_current() -> Union[int, str]:
        """
        """
        data = FPLApiClient().get_json("bootstrap-static")

        current_gws = [gw["id"] for gw in data["events"] if gw["is_current"]]
        return current_gws[0] if current_gws else 'Outside of Season Window'
