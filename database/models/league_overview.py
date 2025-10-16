# Import dependencies
from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from .base import Base

class LeagueOverview(Base):
    __tablename__ = "league_overview"

    id = Column(Integer, primary_key=True)
    event_total = Column(Integer)
    player_name = Column(String(100))
    league_rank = Column(Integer)
    last_rank = Column(Integer)
    rank_sort = Column(Integer)
    total = Column(Integer)
    entry = Column(Integer)
    entry_name = Column(String(100))
    has_played = Column(Boolean)
    bench_boost = Column(Boolean)
    free_hit = Column(Boolean)
    triple_c = Column(Boolean)
    wildcard = Column(Boolean)
    league_name = Column(String(150))
    creation_timestamp = Column(BigInteger)

    def __repr__(self):
        return (
            f"<LeagueOverview(id={self.id}, player_name='{self.player_name}', "
            f"league_name='{self.league_name}', league_rank={self.league_rank}, "
            f"version={self.creation_timestamp})>"
        )
