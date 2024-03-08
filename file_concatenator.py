# Question: Please concatenate 'sample_data_1.txt' and 'sample_data_2.txt'
# to a single text file. The content of the output file should look like below.
# Expected output:
#     x,y
#     3,5
#     4,9
#     6,10
#     7,11
#     8,12
#     6,10
#     8,18
#     12,20
#     14,22
#     16,24

import pandas

data_1 = pandas.read_csv('sample_data_1.txt')

data_2 = pandas.read_csv('sample_data_2.txt')

pandas.concat([data_1, data_2]).to_csv('sample_data_concat.txt', index=None)









