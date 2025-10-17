# Import dependencies
from frontend.functions.mapping import team_colour_map
import re

def test_team_colour_map_contains_expected_teams():
    """
    Test that the colour map contains all expected team names.

    Ensures both Premier League and Championship teams for 2025/26 are present.
    """
    expected_teams = {
        # Premier League
        'Arsenal', 'Liverpool', 'Tottenham Hotspur', 'AFC Bournemouth', 'Manchester City',
        'Crystal Palace', 'Chelsea', 'Everton', 'Sunderland', 'Manchester United',
        'Newcastle United', 'Brighton & Hove Albion', 'Aston Villa', 'Fulham',
        'Leeds United', 'Brentford', 'Nottingham Forest', 'Burnley',
        'West Ham United', 'Wolverhampton Wanderers',

        # Championship
        'Coventry City', 'Middlesbrough', 'Leicester City', 'Preston North End',
        'Stoke City', 'Queens Park Rangers', 'West Bromwich Albion', 'Millwall',
        'Ipswich Town', 'Bristol City', 'Watford', 'Swansea City', 'Charlton Athletic',
        'Portsmouth', 'Hull City', 'Birmingham City', 'Southampton', 'Wrexham',
        'Norwich City', 'Derby County', 'Blackburn Rovers', 'Oxford United',
        'Sheffield Wednesday', 'Sheffield United'
    }

    # Check all expected teams exist in the dictionary
    missing = expected_teams - set(team_colour_map.keys())
    assert not missing, f"Missing teams from colour map: {missing}"


def test_team_colour_map_has_valid_hex_codes():
    """
    Test that each value in the map is a valid 6-character hexadecimal colour code.
    """
    # Define hex pattern
    hex_pattern = re.compile(r"^#[0-9A-Fa-f]{6}$")

    # Ensure all keys have a valid hex code
    for team, colour in team_colour_map.items():
        assert isinstance(colour, str), f"Colour for {team} must be a string"
        assert hex_pattern.match(colour), f"Invalid hex colour for {team}: {colour}"
