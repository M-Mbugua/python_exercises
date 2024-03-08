# Create a script that let the user type in a search term and
# then the program opens the browser and searches the term on Google.

import webbrowser

query = input('Please enter a search query: ')

webbrowser.open(f'https://www.google.com/search?q={query}')


# from googlesearch import search
#
# query = input('Please enter a search query: ')
#
# for i in search(query, tld='com', lang='en', safe='on', num=10, stop=10, pause=2):
#     print(i)


