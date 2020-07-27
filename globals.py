import requests

url = "https://api.covid19india.org/v4/data.json"
dat = requests.get(url).json()
state = 'KA'
district = 'Bengaluru Urban'
