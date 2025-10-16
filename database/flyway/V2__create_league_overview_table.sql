USE [fantasy-premier-league];
GO

CREATE TABLE league_overview (
    id INT IDENTITY(1,1) PRIMARY KEY,
    event_total INT,
    player_name VARCHAR(100),
    league_rank INT,
    last_rank INT,
    rank_sort INT,
    total INT,
    entry INT,
    entry_name VARCHAR(100),
    has_played BIT,
    bench_boost BIT,
    free_hit BIT,
    triple_c BIT,
    wildcard BIT,
    league_name VARCHAR(150)
);

GO
