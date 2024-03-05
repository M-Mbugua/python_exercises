# Question: Please download the file 'company1.json' in the attachment and
# use Python to print out its content.

import json

with open('company1.json', 'r') as f:
    d = json.load(f)

print(d)
