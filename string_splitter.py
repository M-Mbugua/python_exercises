# Question: Create a function that takes any string as input and
# returns the number of words for that string.

def count_words(string):
    string_list = string.split()
    return len(string_list)

print(count_words('How do you do?'))

