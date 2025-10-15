USE [fantasy-premier-league]
GO

CREATE TABLE player_overview (
    id INT PRIMARY KEY,
    second_name VARCHAR(100),
    team VARCHAR(100),
    element_type VARCHAR(50),
    selected_by_percent DECIMAL(5,2),
    now_cost INTEGER,
    minutes INTEGER,
    transfers_in INTEGER,
    value_season DECIMAL(6,2),
    total_points INTEGER,
    goals_scored INTEGER,
    assists INTEGER,
    clean_sheets INTEGER,
    goals_conceded INTEGER,
    own_goals INTEGER,
    penalties_saved INTEGER,
    penalties_missed INTEGER,
    yellow_cards INTEGER,
    red_cards INTEGER,
    saves INTEGER,
    starts INTEGER,
    position VARCHAR(50)
);

GO
