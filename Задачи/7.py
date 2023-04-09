numbers = ['216', '39', '87', '0', '0', '1', '0']
new_numbers = numbers.copy()
for i in range(0, len(numbers) - 1, 2):
    new_numbers[i] = numbers[i + 1]
    new_numbers[i + 1] = numbers[i]
print(" ".join(new_numbers))
