# Question: Create a program that asks the users to submit text
# repeatedly. The program closes when the user enters CLOSE.
# At that point a text file has been created, data.txt, where you
# have all the user submitted values one in each line.

f = open('user_data.txt', 'a+')

while True:

    user_input = input('Enter a value: ')

    if user_input != 'CLOSE':
        f.write(user_input + '\n')
        continue

    else:
        f.close()
        break

