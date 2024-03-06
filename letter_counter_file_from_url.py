# Question: Count the number of "a" characters in this
# text file: http://www.pythonhow.com/data/universe.txt
# Expected output: 47

import requests

response = requests.get("https://pythonhow.com/media/data/universe.txt")
text = response.text
print(text.count('a'))



