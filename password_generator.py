import random

# Setting password lenght
PASSWORD_LENGHT = 12

UPPER_CASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

LOWER_CASE = UPPER_CASE.lower()

NUMBERS = '1234567890'

SYSMBOLS = '!@#$%^*()+[]?'

# Combining uppercase, lowercase, numbers, sysmbols
password_character = UPPER_CASE + LOWER_CASE + NUMBERS + SYSMBOLS

# Creating empty list for random password
password = []

def password_generator():

    for x in range(PASSWORD_LENGHT):
        password.append(random.choice(password_character))

    return ''.join(password)

