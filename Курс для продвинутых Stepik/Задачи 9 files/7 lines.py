with open('lines.txt') as file:
    text = file.readlines()

n = len(max(text, key=len))
print(*filter(lambda x: len(x) == n, text), sep='')