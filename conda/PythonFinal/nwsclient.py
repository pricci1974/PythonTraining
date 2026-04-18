import requests
from config import Config


class NWSClient:
    def __init__(self):
        self.base_url = Config.NWS_URL
        self.headers = {
            "User-Agent": Config.USER_AGENT,
            "Accept": "application/geo+json"
        }

    def get_forecast(self):
        url = f"{self.base_url}"
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                response.raise_for_status()
                data = response.json()
                return data["properties"]["periods"]
            else:
                print(f"Error: Received status code {response.status_code}")
                quit("Error obtaining data")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            quit("Error - exiting program")
            
