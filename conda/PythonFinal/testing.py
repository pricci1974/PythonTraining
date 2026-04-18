import requests

# URL of the API endpoint
url = "https://api.weather.gov/gridpoints/BUF/76,66/forecast"

try:
    # 1. Send an HTTP GET request
    response = requests.get(url, timeout=5.0)
    print(response)
    # 2. Check if the request was successful (status code 200)
    if response.status_code == 200:
        # 3. Parse JSON response into a Python dictionary
        data = response.json()
        
        # Access specific data fields
        #print(f"Title: {data['properties']}")
        for p in data['properties']['periods']:
            print(p['temperature'])
        #print(f"Body: {data['properties']['periods'][0]['number']}")
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")