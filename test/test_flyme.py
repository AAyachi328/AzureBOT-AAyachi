from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from config_test import TestConfig
from msrest.authentication import CognitiveServicesCredentials

CONFIG = TestConfig()

runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)


def test_greetings():

    test_request = "Hi"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "GreetingsIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent

def test_order_travelt():

    test_request = "I need to travel from Tunis"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "OrderTravelIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent

def test_origin_entity():

    test_request = "I need a trip from London"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_origin = "london"
    actual_origin = ""
    if test_response.entities[0].type == 'DepartureCity':
        actual_origin = test_response.entities[0].entity

    assert actual_origin == expected_origin

def test_destination_entity():

    test_request = "I'd like to go to Paris"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_destination = "paris"
    actual_destination = ""
    if test_response.entities[0].type == 'ArrivalCity':
        actual_destination = test_response.entities[0].entity

    assert actual_destination == expected_destination

def test_order_travel_intent_budget_entity():

    test_request = "I can travel for a budget of 500 dollars"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_budget = "500"
    actual_budget = ""
    if test_response.entities[0].type == 'Price':
        actual_budget = test_response.entities[0].entity

    assert actual_budget == expected_budget
