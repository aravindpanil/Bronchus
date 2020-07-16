import json

import globals

with open('dataset.json', 'w') as f:
    json.dump(globals.dat, f)
