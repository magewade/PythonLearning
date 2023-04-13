words = ''
for i in range(int(input())):
    words += str(input().lower())

print(len(set(words)))
