# Question: Create a program that asks the user to enter some values
# separated by commas. And once they use presses enter the program
# will store those values in a text file. If there is no text file a
# new text file will be generated.

data = [str(x) for x in input('Enter values: ').split(', ')]
print(data)

with open('values.txt', 'a+') as f:

    for i in data:
        f.write(i + '\n')

