# Question: Create a script that prints out those countries that have an
# area greater than 2 million square kilometres in the file 'database.db'.

import sqlite3

connection_obj = sqlite3.connect('database.db')
cursor_obj = connection_obj.cursor()
cursor_obj.execute('SELECT country FROM countries WHERE AREA >= 2000000')
rows = cursor_obj.fetchall()

for row in rows:
    print(row[0])

connection_obj.close()

