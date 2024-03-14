# Question: Please use Python to access the database table rows that have
# an area of greater than so an area of 2 million square kilometers or
# greater than that, and then please export those rows to a csv file.

import sqlite3, pandas

connection_obj = sqlite3.connect('database.db')
cursor_obj = connection_obj.cursor()
cursor_obj.execute('SELECT * FROM countries WHERE AREA >= 2000000')
rows = cursor_obj.fetchall()
# print(rows)
connection_obj.close()

dataframe = pandas.DataFrame.from_records(rows)
dataframe.columns = ['Rank', 'Country', 'Area', 'Population']
dataframe.to_csv('countries_area_2_million.csv', index = False)



