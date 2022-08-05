#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os

class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword")
    APP_TYPE = os.environ.get("MicrosoftAppType")
    LUIS_APP_ID = os.environ.get("LuisAppId")
    LUIS_API_KEY = os.environ.get("LuisAPIKey")
    LUIS_API_ENDPOINT = os.environ.get("LuisAPIEndPoint")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey"
    )
