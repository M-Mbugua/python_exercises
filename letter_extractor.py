# Question: Write a script that extracts letters from 'letters.zip'
# and prints them out as a list.

import glob
from zipfile import ZipFile

zip_obj = ZipFile('letters.zip', 'r')
zip_obj.extractall('extracted_letters')
letters = []
files = glob.glob('extracted_letters/letters/*.txt')

for file in files:
    with open(file, 'r') as f:
        letters.append(f.read().strip('\n'))

print(letters)

