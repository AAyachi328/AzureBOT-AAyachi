from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from config import DefaultConfig
from msrest.authentication import CognitiveServicesCredentials

CONFIG = DefaultConfig()

runtime_credentials = CognitiveServicesCredentials(CONFIG.LUIS_API_KEY)
client_runtime = LUISRuntimeClient(endpoint=CONFIG.LUIS_API_ENDPOINT, credentials=runtime_credentials)


def test_greetings_intent():

    test_request = "Hello"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "GreetingsIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent


def test_none_intent():

    test_request = "I want to rent a car"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "NoneIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent


def test_order_travel_intent():

    test_request = "I need to book a flight"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_intent = "OrderTravelIntent"
    actual_intent = test_response.top_scoring_intent.intent
    assert actual_intent == expected_intent


def test_order_travel_intent_origin_entity():

    test_request = "I need a trip from Busan"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_origin = "busan"
    actual_origin = ""
    if test_response.entities[0].type == 'DepartureCity':
        actual_origin = test_response.entities[0].entity

    assert actual_origin == expected_origin


def test_order_travel_intent_destination_entity():

    test_request = "I'd like to go to Caprica"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_destination = "caprica"
    actual_destination = ""
    if test_response.entities[0].type == 'ArrivalCity':
        actual_destination = test_response.entities[0].entity

    assert actual_destination == expected_destination


def test_order_travel_intent_travel_dates_entity():

    test_request = "I would like to book a travel from 15 November 2021 to 15 December 2021"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_start_travel_date = "15 november 2021"
    actual_start_travel_date = ""
    if test_response.entities[1].type == 'DepartureDate':
        actual_start_travel_date = test_response.entities[1].entity

    expected_end_travel_date = "15 december 2021"
    actual_end_travel_date = ""
    if test_response.entities[0].type == 'ArrivalDate':
        actual_end_travel_date = test_response.entities[0].entity

    assert actual_start_travel_date == expected_start_travel_date
    assert actual_end_travel_date == expected_end_travel_date


def test_order_travel_intent_budget_entity():

    test_request = "I'd like to book a trip and I have a budget of 1000 usd"
    test_response = client_runtime.prediction.resolve(CONFIG.LUIS_APP_ID, query=test_request)

    expected_budget = "1000 usd"
    actual_budget = ""
    if test_response.entities[0].type == 'Price':
        actual_budget = test_response.entities[0].entity

    assert actual_budget == expected_budget
