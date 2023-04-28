import random

with open("first_names.txt") as f_names, open("last_names.txt") as s_names:
    n = 3
    names = [i.strip() for i in f_names.readlines()]
    surnames = [i.strip() for i in s_names.readlines()]
    for i in range(n):
        print(random.choice(names), random.choice(surnames))