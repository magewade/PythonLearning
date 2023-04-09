numbers = input()
numbers_list = numbers.split()
counter = 0
for i in range(len(numbers_list) - 1):
    if int(numbers_list[i + 1]) > int(numbers_list[i]):
        counter += 1
print(counter)