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
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data["properties"]["periods"]
    
