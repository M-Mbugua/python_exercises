# Question: Please generate at list from 1 to 20 but do not create the list manually.

lst = list(range(1,21))

print(lst)

# Question: Complete the script so that it produces the expected output.
# Please use my_range as input data.
# Expected output:
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

my_range = range(1, 21)

print([10 * n for n in my_range])

# Question: Complete the script, so it generates the expected output using my_range  as input
# data. Please note that the items of the expected list output are all strings.
#  Expected output:
#
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

my_range = range(1, 21)

print([str(n) for n in my_range])
print(list(map(str, my_range)))





