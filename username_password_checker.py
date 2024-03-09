# Create a program that asks the user to enter a username and password.
# Check that the username does not exist in 'usernames.txt'.
# Check that the submitted password should contain at least
# one number, one uppercase letter, and at least 5 characters.
# If the conditions are met, print out the reason why pointing
# to the specific condition/s that has not been satisfied.

print("Please create a password that contains at least one number,"
      "one uppercase letter, and have at least 5 characters.")
i = 0
while i < 1:

    username = input("Please enter a username: ")

    with open('usernames.txt', 'r') as f:
        usernames = f.read()
        # usernames = f.readlines()
        # usernames = [u.strip('\n') for u in users]

    if username in usernames:
        print("Username exists!")
        continue

    else:
        print("Username is fine.")
        break


while True:

    messages = []
    password = input("Enter your password: ")

    if not any(ch.isdigit() for ch in password):
        messages.append("Password must contain at least one number!")

    if not any(ch.isupper() for ch in password):
        messages.append("Password must contain at least one uppercase letter!")

    if len(password) < 5:
        messages.append("Password must have at least 5 characters!")

    if len(messages) == 0:
        print("Password is fine.")
        break

    else:
        print("Please check the following: ")
        for message in messages:
            print(message)




