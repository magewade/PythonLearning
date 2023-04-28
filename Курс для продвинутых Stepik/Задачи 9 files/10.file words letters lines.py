from functools import reduce

with open("file.txt") as file:
    letters = 0
    words = 0
    lines = 0
    for line in file:
        file.seek(0)
        words = len(file.read().split())
    file.seek(0)
    for line in file:
        letters += reduce(lambda x, y: x + y, list(map(lambda x: x.isalpha(), line)))
        lines += 1

    print('Input file contains:')
    print(f'{letters} letters')
    print(f'{words} words')
    print(f'{lines} lines')
