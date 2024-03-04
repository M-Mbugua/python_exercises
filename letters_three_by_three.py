# Question: Create a script that generates a file where all letters of the
# English alphabet are listed three in each line. The inside of the text
# file would look like:
# abc
# def
# ghi ...and so on.

import string


f = open('letters_three.txt', 'w')
letters = string.ascii_lowercase + ' '
first = letters[::3]
second = letters[1::3]
third = letters[2::3]

for x, y, z in zip(first, second, third):
    f.write(x + y + z + '\n')

f.close()





