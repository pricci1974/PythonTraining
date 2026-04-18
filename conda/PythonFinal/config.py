# This file stores the url address and user info
# for accessing the NWS API. This is a free service and no key is required
# however they do need proper headers

class Config:
    NWS_URL = "https://api.weather.gov/gridpoints/BUF/76,66/forecast"
    USER_AGENT = "weather-app (pdr1974@gmail.com)"