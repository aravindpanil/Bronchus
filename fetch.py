from datetime import date, timedelta, datetime

import globals

state = 'Karnataka'
district = 'Bengaluru Urban'
data = list()

tdy = date.today()
ydy = tdy - timedelta(days=1)


def data_by_date(dateval):
    for item in globals.dat['districtsDaily'][state][district]:
        if datetime.strptime(item['date'], '%Y-%m-%d').date() == dateval:
            # item['date'] is stored as a string. using strptime to convert to datetime and
            # date() to convert to date so that comparison with dateval can be done
            return item


def fetch_data(*arg):
    for item in arg:
        data.append(data_by_date(item))


fetch_data(tdy, ydy)

if data[0] is None:
    tdy = ydy
    ydy = ydy - timedelta(days=2)
    data.clear()
    fetch_data(tdy, ydy)

elif data[0]['confirmed'] <= data[1]['confirmed']:
    tdy = ydy
    ydy - timedelta(days=1)
    data.clear()
    fetch_data(tdy, ydy)

wkdy = tdy - timedelta(weeks=1)
fetch_data(wkdy)

daily_cases = data[0]['active'] - data[1]['active']
daily_deaths = data[0]['deceased'] - data[1]['deceased']
weekly_cases = data[0]['active'] - data[2]['active']
weekly_deaths = data[0]['deceased'] - data[2]['deceased']

print("New cases today (", tdy, ") -", daily_cases)
print("Deaths today (", tdy, ") -", daily_deaths)
print("New cases in the last 7 days -", weekly_cases)
print("Deaths this week -", weekly_deaths)
