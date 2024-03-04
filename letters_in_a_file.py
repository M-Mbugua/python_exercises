# Question: Create a script that generates a text file with all letters of the
# English alphabet inside it, one letter per line.

import string

f = open('letters.txt', 'w')

for letter in string.ascii_lowercase:
    f.write(f'{letter}\n')

f.close()

