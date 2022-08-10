#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os

class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId","7a91cf0e-f863-4afa-90a0-9f33276049f4")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword","Ptf8Q~IkHyzJDTQV3~g3R26t2rIEnJohIp61-coj")
    LUIS_APP_ID = os.environ.get("LuisAppId", "987333db-27f7-48f8-87ec-5be5e584df98")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "02d3280f9d6f48a2ad7e532e95d09e4b")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    LUIS_API_ENDPOINT = os.environ.get("LuisAPIEndPoint", "https://ayachip10luis.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey","7c6360fb-0ba2-493a-bf25-c90a3c0ff66c"
    )
