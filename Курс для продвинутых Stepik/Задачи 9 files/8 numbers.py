with open('numbers.txt') as f:
    for line in f:
        print(sum(map(int, line.split())))