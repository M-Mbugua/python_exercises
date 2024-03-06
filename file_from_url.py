# Question: Print out the text of this file https://pythonhow.com/media/data/universe.txt
# Don't manually download the file. Let Python do all the work.

import requests

response = requests.get("https://pythonhow.com/media/data/universe.txt")
print(response.text)
