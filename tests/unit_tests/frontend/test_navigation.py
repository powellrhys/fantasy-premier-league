# Import dependencies
from frontend.functions.navigation import get_navigation
from unittest.mock import patch, MagicMock

def test_get_navigation():
    """
    Test that get_navigation() builds the correct navigation structure using
    mocked Streamlit components and returns the expected navigation object.
    """

    # Patch Streamlit components inside the target module
    with patch("frontend.functions.navigation.st.Page") as mock_page, \
         patch("frontend.functions.navigation.st.navigation") as mock_navigation:

        # Arrange: configure the mocks
        mock_page.side_effect = lambda *args, **kwargs: MagicMock()
        mock_navigation.return_value = "fake_navigation_object"

        # Act: execute the function
        result = get_navigation()

        # Assert: verify the returned value
        assert result == "fake_navigation_object", "Expected get_navigation() to return mocked navigation object"

        # st.Page should be called once for each page defined (1 + 3 + 1 = 5)
        assert mock_page.call_count == 5, f"Expected 5 Page calls, got {mock_page.call_count}"

        # st.navigation should be called exactly once
        mock_navigation.assert_called_once()

        # Extract the argument passed to st.navigation (the pages dict)
        pages_arg = mock_navigation.call_args[0][0]

        # Verify all top-level navigation groups exist
        expected_sections = {"Home", "Club & Player Analysis", "Chip Analysis"}
        assert expected_sections.issubset(pages_arg.keys()), \
            f"Missing sections in navigation: {expected_sections - pages_arg.keys()}"

        # Verify that each section has at least one Page object
        for section, pages in pages_arg.items():
            assert isinstance(pages, list), f"Expected list of pages for section '{section}'"
            assert all(isinstance(p, MagicMock) for p in pages), \
                f"Expected all entries in '{section}' to be mocked Page objects"
