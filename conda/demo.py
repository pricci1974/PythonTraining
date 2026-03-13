import requests, os
url = "https://api.github.com/repos/python/cpython"
r = requests.get(url, timeout=10)
r.raise_for_status()
data = r.json()
print(data["stargazers_count"])