import requests
from behave import given, then

BASE_URL = "https://catfact.ninja"

@given('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    context.response = requests.get(BASE_URL + endpoint)
    context.json_data = context.response.json()

@then('the response status should be {status_code:d}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, but got {context.response.status_code}"

@then('the response should contain "{key}" with value {value:d}')
def step_check_json_value(context, key, value):
    assert context.json_data.get(key) == value, \
        f"Expected {key} to be {value}, but got {context.json_data.get(key)}"

@then('the last breed in the list should be "{expected_breed}"')
def step_check_last_breed(context, expected_breed):
    last_breed = context.json_data["data"][-1]["breed"]
    assert last_breed == expected_breed, \
        f"Expected last breed to be {expected_breed}, but got {last_breed}"

@then('the response should contain exactly {count:d} breeds')
def step_check_breed_count(context, count):
    assert len(context.json_data["data"]) == count, \
        f"Expected {count} breeds, but got {len(context.json_data['data'])}"

@then('the list should start from item {expected_start:d}')
def step_check_starting_item(context, expected_start):
    assert context.json_data.get("from") == expected_start, \
        f"Expected list to start at {expected_start}, but got {context.json_data.get('from')}"

@then('the last page should be {expected_page:d}')
def step_check_last_page(context, expected_page):
    assert context.json_data.get("last_page") == expected_page, \
        f"Expected last page to be {expected_page}, but got {context.json_data.get('last_page')}"

@then('the response should contain an empty list')
def step_check_empty_list(context):
    assert len(context.json_data["data"]) == 0, \
        f"Expected empty list, but got {len(context.json_data['data'])} items"
