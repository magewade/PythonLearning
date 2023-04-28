import random

with open("input.txt", "r") as input_f, open("output.txt", "w") as output_f:
    count = 1
    for line in input_f:
        print(f'{count}) ' + line, file=output_f, end='')
        count += 1