# Question: Create a script that reads this file, multiplies
# its values by two, and saves the output in a new text file.

import pandas

data = pandas.read_csv('data.txt')

data_2 = data * 2

data_2.to_csv("data_multiplied.txt", index=None)

