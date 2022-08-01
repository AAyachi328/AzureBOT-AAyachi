#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os

class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "7a91cf0e-f863-4afa-90a0-9f33276049f4")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "gQO8Q~H49QYmn5BWdRDULvVdcEAFMtKF23nUBc4t")
    LUIS_APP_ID = os.environ.get("LuisAppId", "344ec82a-9bb8-40cc-a18c-5e6b86ae28b2")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "124604c7b30c4a24874fb88553d7652f")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey"
    )
