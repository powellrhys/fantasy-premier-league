# Import dependencies
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, BigInteger
from .base import Base

class PlayerOverview(Base):
    __tablename__ = "player_overview"

    id = Column(Integer, primary_key=True)
    web_name = Column(String(100))
    team = Column(String(100))
    element_type = Column(String(50))
    selected_by_percent = Column(DECIMAL(5, 2))
    now_cost = Column(Integer)
    minutes = Column(Integer)
    transfers_in = Column(Integer)
    value_season = Column(DECIMAL(6, 2))
    total_points = Column(Integer)
    goals_scored = Column(Integer)
    assists = Column(Integer)
    clean_sheets = Column(Integer)
    goals_conceded = Column(Integer)
    own_goals = Column(Integer)
    penalties_saved = Column(Integer)
    penalties_missed = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    saves = Column(Integer)
    starts = Column(Integer)
    position = Column(String(50))
    photo = Column(String(255))
    in_dreamteam = Column(Boolean)
    defensive_contribution_per_90 = Column(DECIMAL(5, 2))
    creation_timestamp = Column(BigInteger)

    def __repr__(self):
        return (
            f"<PlayerOverview(id={self.id}, name={self.web_name}, "
            f"team={self.team}, version={self.creation_timestamp})>"
        )
