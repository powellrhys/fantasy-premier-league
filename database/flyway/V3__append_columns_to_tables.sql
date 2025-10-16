-- Rename column second_name → web_name
EXEC sp_rename 'player_overview.second_name', 'web_name', 'COLUMN';

-- Add new columns player_overview table
ALTER TABLE player_overview
ADD
    photo VARCHAR(255),
    in_dreamteam BIT,
    defensive_contribution_per_90 DECIMAL(5,2),
    creation_timestamp BIGINT NULL;

-- Add new column to league_overview table
ALTER TABLE league_overview
ADD
    creation_timestamp BIGINT NULL;
