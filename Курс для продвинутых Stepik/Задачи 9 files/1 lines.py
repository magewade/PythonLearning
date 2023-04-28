import random

file = open("lines.txt", "r")
content = file.readlines()
print(content)
print(random.choice(content))

file.close()


