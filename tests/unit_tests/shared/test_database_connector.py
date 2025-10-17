# Import dependencies
from shared.functions.sql.database_connector import DatabaseConnector
from unittest.mock import patch, MagicMock
import pytest

def test_database_connector_init_success():
    """
    Test successful initialization of DatabaseConnector.
    """
    with patch("shared.functions.sql.database_connector.Variables") as mock_vars, \
         patch("shared.functions.sql.database_connector.create_engine") as mock_create_engine, \
         patch("shared.functions.sql.database_connector.sessionmaker") as mock_sessionmaker:

        # Mock Variables to return a database_connection_string
        mock_vars.return_value.database_connection_string = "fake_connection_string"

        # Mock engine and session
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session

        # Initialize connector
        connector = DatabaseConnector(source="backend")

        # Assert Variables initialized with correct source
        mock_vars.assert_called_once_with(source="backend")

        # Assert engine created with correct connection string
        mock_create_engine.assert_called_once_with("fake_connection_string")
        assert connector.engine == mock_engine

        # Assert sessionmaker created
        mock_sessionmaker.assert_called_once_with(bind=mock_engine)
        assert connector.Session == mock_sessionmaker.return_value


def test_database_connector_missing_connection_string():
    """
    Test that initialization fails if database_connection_string is missing.
    """
    with patch("shared.functions.sql.database_connector.Variables") as mock_vars:
        mock_vars.return_value.database_connection_string = None

        with pytest.raises(ValueError, match="database_connection_string not found in environment variables"):
            DatabaseConnector(source="backend")
