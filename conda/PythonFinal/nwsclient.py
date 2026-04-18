# This file is used to communicate with the NWS API

import requests
from config import Config


class NWSClient:
    def __init__(self): # This configures the request and headers
        self.base_url = Config.NWS_URL
        self.headers = {
            "User-Agent": Config.USER_AGENT,
            "Accept": "application/geo+json"
        }

# This function obtains the data and returns the forecast portion. The properties
# contain a list of periods of which must be iterated through to obtain
# the temperature and name data for each of the periods
    def get_forecast(self):
        url = f"{self.base_url}"
        try: # Try/catch is needed to safely exit program if there is an error
            # There are times when the NWS server is down
            response = requests.get(url, headers=self.headers)
            # This if statemend ensures data is actually received before proceeding
            # If there is no data, then the program must exit
            if response.status_code == 200:
                response.raise_for_status()
                data = response.json() #This puts the data in json format
                return data["properties"]["periods"] # returns the blocks of days
            else:
                print(f"Error: Received status code {response.status_code}")
                quit("Error obtaining data")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            quit("Error - exiting program")
            
