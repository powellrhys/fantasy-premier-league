# Import dependencies
from backend.functions.data.manager import Manager
from behave import given, when, then
from unittest.mock import patch


@given('a manager with ID {manager_id:d}')
def step_given_manager(context, manager_id):
    """
    Create a Manager instance for testing.

    This step initializes a `Manager` object using the provided
    `manager_id`. The created instance is stored in the Behave
    context object so it can be reused by later steps in the scenario.
    """
    context.manager = Manager(manager_id)


@given('the API returns chips "{chip_list}"')
def step_given_api_returns_chips(context, chip_list):
    """
    Mock the FPL API response to return a predefined list of chips.

    This step simulates the Fantasy Premier League API by creating a
    fake JSON response containing a list of chip names (e.g.,
    "bboost", "3xc", "wildcard"). It cleans and normalizes the input
    chip list string from the feature file so it can be properly parsed.
    The response is stored in the Behave context object for later use.
    """
    # Normalize variations such as `"bboost", "3xc", and "wildcard"`
    clean_list = (
        chip_list.replace(" and ", ",")
        .replace("'", "")
        .replace('"', "")
    )

    # Split by commas and strip whitespace
    chips = [chip.strip() for chip in clean_list.split(",") if chip.strip()]

    # Mocked API response structure
    context.fake_api_response = {"chips": [{"name": c} for c in chips]}


@given('the API returns no chips')
def step_given_api_returns_no_chips(context):
    """
    Mock the FPL API response with an empty chip list.

    This step ensures that when the Manager retrieves data,
    the mock API returns an empty `chips` array. It allows testing
    scenarios where the manager has not used any chips yet.
    """
    context.fake_api_response = {"chips": []}


# --- When Steps ---


@when('the chip flags are retrieved')
def step_when_get_chip_flags(context):
    """
    Retrieve the chip usage flags using a mocked API response.

    This step patches the `FPLApiClient.get_json()` method inside
    the Manager class to return the mocked API response created
    in the previous step. It then calls `get_chip_flags()` on the
    Manager instance and stores the resulting dictionary in the
    Behave context object for later assertions.
    """
    with patch("backend.functions.data.manager.FPLApiClient.get_json", return_value=context.fake_api_response):
        context.result = context.manager.get_chip_flags()


# --- Then Steps ---


@then('the bench boost flag should be {expected:d}')
def step_then_bench_boost_flag(context, expected):
    """
    Verify that the bench boost flag matches the expected value.

    This step asserts that the `bench_boost` flag returned by
    `get_chip_flags()` equals the expected integer value (0 or 1).
    """
    assert context.result["bench_boost"] == expected


@then('the free hit flag should be {expected:d}')
def step_then_free_hit_flag(context, expected):
    """
    Verify that the free hit flag matches the expected value.

    This step checks whether the `free_hit` flag from the Manager's
    chip flag dictionary matches the expected integer value (0 or 1).
    """
    assert context.result["free_hit"] == expected


@then('the triple captain flag should be {expected:d}')
def step_then_triple_c_flag(context, expected):
    """
    Verify that the triple captain flag matches the expected value.

    This step asserts that the `triple_c` flag in the Manager’s
    chip usage dictionary equals the provided expected value.
    """
    assert context.result["triple_c"] == expected


@then('the wildcard flag should be {expected:d}')
def step_then_wildcard_flag(context, expected):
    """
    Verify that the wildcard flag matches the expected value.

    This step ensures that the Manager correctly identifies
    whether the wildcard chip was used based on the mocked data.
    """
    assert context.result["wildcard"] == expected


@then('all chip flags should be 0')
def step_then_all_flags_zero(context):
    """
    Verify that all chip flags are zero.

    This step is used for scenarios where the manager has not
    used any chips. It loops through the chip flag dictionary
    (excluding the `entry` key) and asserts that all values are 0.
    """
    assert all(v == 0 for k, v in context.result.items() if k != "entry")
