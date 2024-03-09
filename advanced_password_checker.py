# Create a program that asks the user to enter a new password
# and check that the submitted password should contain at least
# one number, one uppercase letter, and at least 5 characters.
# If the conditions are met, print out the reason why pointing
# to the specific condition/s that has not been satisfied.

print("Please create a password that contains at least one number,"
      "one uppercase letter, and have at least 5 characters.")

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



