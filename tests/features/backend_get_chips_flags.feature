Feature: Manager Chip Usage Flags
  As a Fantasy Premier League analyst
  I want to determine which chips a manager has used
  So that I can understand their gameweek strategy

  Scenario: Manager has used multiple chips
    Given a manager with ID 123
    And the API returns chips "bboost", "3xc", and "wildcard"
    When the chip flags are retrieved
    Then the bench boost flag should be 1
    And the free hit flag should be 0
    And the triple captain flag should be 1
    And the wildcard flag should be 1

  Scenario: Manager has not used any chips
    Given a manager with ID 456
    And the API returns no chips
    When the chip flags are retrieved
    Then all chip flags should be 0
