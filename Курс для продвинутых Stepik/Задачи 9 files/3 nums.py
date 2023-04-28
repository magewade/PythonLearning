file = open("nums.txt", "r")
result = 0
for line in file:
    if line != "\n" and line.strip().isdigit():
        result += int(line)
print(result)
file.close()



