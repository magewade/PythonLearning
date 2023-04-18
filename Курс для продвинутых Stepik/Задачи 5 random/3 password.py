import string
import random

lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
lower_letters.remove("l")
upper_letters.remove("I")
lower_letters.remove("o")
upper_letters.remove("O")
numbers = list("23456789")

n, m = int(input()), int(input())
plus = lower_letters.copy()
plus.extend(upper_letters)
plus.extend(numbers)

def generate_password(m):
    password = ""
    if random.randint(1, 3) == 1:
        password += random.choice(lower_letters)
        password += random.choice(numbers)
        password += random.choice(upper_letters)
    elif random.randint(1, 3) == 2:
        password += random.choice(numbers)
        password += random.choice(lower_letters)
        password += random.choice(upper_letters)
    else:
        password += random.choice(upper_letters)
        password += random.choice(lower_letters)
        password += random.choice(numbers)

    for _ in range(m - 3):
        password += random.choice(plus)

    return password

for i in range(n):
    print(generate_password(m))