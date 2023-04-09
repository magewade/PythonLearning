numbers = input().split()
num_set = set(numbers)
print(len(num_set))


counter = 1
for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        counter += 1
print(counter)
