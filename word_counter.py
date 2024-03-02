# Question: Please download the words1.txt file from the attachment
# and then create a Python function that takes a text file as input
# and returns the number of words contained in the text file.
# Expected output: 10

def count_words(file):
    f = open(file,'r')
    string = f.read()
    words = string.split()
    return len(words)


print(count_words('words1.txt'))
