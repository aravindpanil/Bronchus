import globals

data = globals.dat

today_data = data[globals.state]['districts'][globals.district]['delta']
last_updated = data[globals.state]['districts'][globals.district]['meta']['tested']['last_updated']

print('Information Last Updated on - ', last_updated)
print('Total deaths - ', today_data['deceased'])
print('Total Confirmed - ', today_data['confirmed'])
print('Total Recovered - ', today_data['recovered'])
