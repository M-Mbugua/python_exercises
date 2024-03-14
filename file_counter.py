# Question: Please download the attached ZIP file 'files.zip' and extract
# its files in a folder. Then, write a script that counts and prints out
# the number of .py files in that folder.
# Expected output:
#       2

import glob

files = glob.glob('files/*.py')

print(len(files))





