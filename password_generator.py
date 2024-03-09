# Create a program that generates a password of 6 random
# alphanumeric characters.

import random, string

characters = string.ascii_letters + '!@#$%^&*()?'

password = random.sample(characters, k=6)

print(''.join(password))
