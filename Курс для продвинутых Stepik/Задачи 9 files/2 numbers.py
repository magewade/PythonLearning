file = open("numbers.txt", "r")
result = 0
for line in file:
    result += int(line)
print(result)
file.close()


# print(sum(map(int, file)))



