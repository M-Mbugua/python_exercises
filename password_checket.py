# Create a program that asks the user to enter a new password
# and check that the submitted password should contain at least
# one number, one uppercase letter, and at least 5 characters.
# If the conditions are generated, print out "Password is fine";
# otherwise, keep prompting the user for a password.

print("Please create a password that contains at least one number,"
      "one uppercase letter, and have at least 5 characters.")

while True:

    password = input("Enter your password: ")

    if any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password) and len(password) >= 5:
        print("Password is fine")
        break

    else:
        print("Password must satisfy all conditions!")
