from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from .config import DefaultConfig
from msrest.authentication import CognitiveServicesCredentials

CONFIG = DefaultConfig()

runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)


def test_greetings():

    test_request = "Hello"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "GreetingsIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent

def test_order_travelt():

    test_request = "I need to book a flight"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "OrderTravelIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent

def test_origin_entity():

    test_request = "I need a trip from Busan"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_origin = "busan"
    actual_origin = ""
    if test_response.entities[0].type == 'DepartureCity':
        actual_origin = test_response.entities[0].entity

    assert actual_origin == expected_origin

def test_destination_entity():

    test_request = "I'd like to go to Caprica"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_destination = "caprica"
    actual_destination = ""
    if test_response.entities[0].type == 'ArrivalCity':
        actual_destination = test_response.entities[0].entity

    assert actual_destination == expected_destination

def test_order_travel_intent_budget_entity():

    test_request = "I'd like to book a trip and I have a budget of 1000 usd"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_budget = "1000 usd"
    actual_budget = ""
    if test_response.entities[0].type == 'Price':
        actual_budget = test_response.entities[0].entity

    assert actual_budget == expected_budget
