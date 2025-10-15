# Import dependencies
from sqlalchemy import Column, Integer, String, DECIMAL
from .base import Base

class PlayerOverview(Base):
    __tablename__ = "player_overview"

    id = Column(Integer, primary_key=True)
    second_name = Column(String(100))
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

    def __repr__(self):
        return f"<Player(id={self.id}, name={self.second_name}, team={self.team}, position={self.position})>"
