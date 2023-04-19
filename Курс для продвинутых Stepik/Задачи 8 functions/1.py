def square(x):

    return x**2

numbers = [1, 2, 3, 4]

something = list(map(lambda x: square(x), numbers))

print(something[2])