#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os

class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId","")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword","")
    LUIS_APP_ID = os.environ.get("LuisAppId", "987333db-27f7-48f8-87ec-5be5e584df98")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "02d3280f9d6f48a2ad7e532e95d09e4b")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName","")
    LUIS_API_ENDPOINT = os.environ.get("LuisAPIEndPoint","")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey",""
    )
