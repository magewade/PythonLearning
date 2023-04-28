file = open("prices.txt", "r")
result = 0
for line in file:
    line_data = line.split("\t")
    result += int(line_data[2]) * int(line_data[1])
print(result)