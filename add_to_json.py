# Question: Please download the json file in the attachment and
# use Python to add a new employee to the file's content.

import json

with open('company2.json', 'r+') as f:
    d = json.load(f)
    d['employees'].append(dict(firstName = 'Albert', lastName = 'Bert'))
    f.seek(0)
    json.dump(d, f, indent=4)


