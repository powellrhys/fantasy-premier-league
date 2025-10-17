# Import dependencies
from shared.functions.variables import Variables
from unittest.mock import patch
import pytest

class TestVariables:

    def test_variables_backend_source(self, monkeypatch):
        """
        Verify Variables with source='backend'.

        Ensures environment variables are read correctly,
        attributes are assigned, and dict-like access works.
        """
        # Mock environment variables
        monkeypatch.setenv("database_connection_string", "fake_db_conn")
        monkeypatch.setenv("league_ids", "1, 2, 3")

        # Initialize Variables object using 'backend' source
        vars_obj = Variables(source="backend")

        # Verify attributes are correctly assigned
        assert vars_obj.database_connection_string == "fake_db_conn"
        assert vars_obj.league_ids == [1, 2, 3]

        # Test dict-like access returns correct values
        assert vars_obj["database_connection_string"] == "fake_db_conn"
        assert vars_obj["league_ids"] == [1, 2, 3]

        # Accessing a nonexistent key raises KeyError
        with pytest.raises(KeyError):
            _ = vars_obj["nonexistent_key"]

    def test_variables_backend_source_empty_league_ids(self, monkeypatch):
        """
        Verify that empty 'league_ids' environment variable results in empty list.
        """
        # Prevent load_dotenv from reading your real .env file
        monkeypatch.setattr("shared.functions.variables.variables.load_dotenv", lambda: None)

        # Delete league_ids if exists
        monkeypatch.delenv("league_ids", raising=False)
        # Set database_connection_string manually
        monkeypatch.setenv("database_connection_string", "fake_db_conn2")

        # Initialize Variables; now it won't read your real .env
        vars_obj = Variables(source="backend")

        assert vars_obj.league_ids == []  # empty list as expected
        assert vars_obj.database_connection_string == "fake_db_conn2"

    def test_variables_streamlit_source(self):
        """
        Verify Variables with source='streamlit'.

        Ensures Streamlit secrets are read correctly and attributes are assigned.
        """
        # Define fake Streamlit secrets
        fake_secrets = {
            "general": {
                "database_connection_string": "secret_db_conn",
                "privileged_users": "powellrhys",
            }
        }

        # Patch Streamlit module to use fake secrets
        with patch("shared.functions.variables.variables.st") as mock_st:
            mock_st.secrets = fake_secrets

            # Initialize Variables object with 'streamlit' source
            vars_obj = Variables(source="streamlit")

            # Verify attributes are correctly loaded from secrets
            assert vars_obj.database_connection_string == "secret_db_conn"
            assert vars_obj.privileged_users == ["powellrhys"]

            # Dict-like access works
            assert vars_obj["database_connection_string"] == "secret_db_conn"
            assert vars_obj["privileged_users"] == ["powellrhys"]

            # Accessing a nonexistent key raises KeyError
            with pytest.raises(KeyError):
                _ = vars_obj["nonexistent_key"]
