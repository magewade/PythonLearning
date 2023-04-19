numbers = "489 483 43 2 3 84 1 4 3 2 5 4 3 13".split()
print(len(numbers))
new_numbers = [numbers[len(numbers) - 1], numbers[0:len(numbers) - 1]]
print(new_numbers)
print(new_numbers[0], ' '.join(new_numbers[1]))
