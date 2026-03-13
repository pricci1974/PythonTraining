import requests
from requests.exceptions import Timeout
# Program uses requests to connect to external API to obtain data. The API is free to use
# w/o authorization. This program obtains sunrise/sunset data based on the lattitude and
# longitude of western NY. The times have been requested for New York.

print("This program obtains sunrise and sunset data for Western NY from sunrise-sunset.org")

input("Press ENTER to contine") # Pause the program to give user a chance to read introduction

url = 'https://api.sunrise-sunset.org/json?lat=43.346867&lng=-78.224558&tzid=America/New_York'

# This try/except block is used to account for connection errors. Added a specific block
# in the event the request times out
try:

    response = requests.get(url, timeout=5)
    

    if response.status_code == 200: # Statud code 200 indicates a successful response from server
        # this converts the data to json format
        data = response.json()

        # assigns the important elements of the data to varables
        sunrise = data['results']['sunrise']
        sunset = data['results']['sunset']
        # display message in meaningful format to user
        print(f'The sunrise today is {sunrise} and the sunset is {sunset}',
              'courtesy of sunrise-sunset.org')
    else:
        # message to user if API server did not respond correctly
        print("Could not retreive sunrise/sunset data, please try again later.")

# Exception messages based on general failure or time out
except Exception:
    print(f'Could not connect to API')

except Timeout:
    print(f'Connection Timed Out')