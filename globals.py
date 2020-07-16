import requests

url = "https://api.covid19india.org/districts_daily.json"
dat = requests.get(url).json()
