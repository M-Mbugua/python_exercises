# Question: Create a script that generates a file where all letters of
# the English alphabet are listed two in each line. The inside of the
# text file would look like:
# ab
# cd
# ef   ...and so on.

import string


f = open('letters_two.txt', 'w')
first = string.ascii_lowercase[::2]
second = string.ascii_lowercase[1::2]

for x,y in zip(first, second):
    f.write(x + y + '\n')

f.close()

