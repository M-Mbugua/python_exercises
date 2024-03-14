# Question: Create a script to add the rows of ten_more_countries to the database file.
# The text file does not have a population column and therefore these would be NULL.

import sqlite3, pandas

data = pandas.read_csv('ten_more_countries.txt')

connection_obj = sqlite3.connect('database1.db')
cursor_obj = connection_obj.cursor()

for index, row in data.iterrows():
    cursor_obj.execute('INSERT INTO countries VALUES (NULL, ?, ?, NULL)', (row['Country'], row['Area']))

connection_obj.commit()
connection_obj.close()


