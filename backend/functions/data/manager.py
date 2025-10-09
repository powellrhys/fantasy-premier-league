# Import dependencies
from .fpl_api_client import FPLApiClient

class Manager:
    def __init__(self, manager_id: int):
        self.manager_id = manager_id

    def get_chip_flags(self) -> dict:
        data = FPLApiClient().get_json(f"entry/{self.manager_id}/history/")
        chips = [chip["name"] for chip in data.get("chips", [])]
        return {
            "entry": self.manager_id,
            "bench_boost": int("bboost" in chips),
            "free_hit": int("freehit" in chips),
            "triple_c": int("3xc" in chips),
            "wildcard": int("wildcard" in chips)
        }
