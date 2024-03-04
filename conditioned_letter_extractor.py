# Question: Write a script that iterates through each of the 26 text files
# and checks whether the letter inside the text file is in string 'python'
# and then puts the letter in a list if the letters is.

import glob

letters = []
python = 'python'
files = glob.glob('extracted_letters/letters/*.txt')

for file in files:
    with open(file, 'r') as f:
        letter = f.read().strip('\n')

    if letter in python:
        letters.append(letter)


print(letters)
