import config
import requests
import json
import tool_logging as log

logger = log.create_logger(__name__,'weather_app.log')

class Weather:
    def __init__(self):
        logger.debug(f"Initialising Weather Class")

class Location:
    def __init__(self):
        logger.debug(f"Initialising Location Class")

if config.api["real_run"]:
    resp = requests.get(path, params=params)
    if resp.status_code != 200:
        # This means something went wrong.
        print(f"GET {config.api_paths_forecast['forecast_1_hour']} {resp.status_code}")
else:
    logger.debug(f"Real run set to False, printing test statement")
    print("Here's an example response")