# Question: Create a program that asks the users to submit text
# repeatedly. The input is saved in a text file when the user enters SAVE
# but the file is not closed. The file is closed when the user enters CLOSE
# and the program ends.

f = open('user_data1.txt', 'a+')

while True:

    user_input = input('Enter a value: ')

    if user_input == 'CLOSE':
        f.close()
        break

    elif user_input == 'SAVE':
        f.close()
        f = open('user_data1.txt', 'a+')

    else:
        f.write(user_input + '\n')





