with open("data.txt") as data:
    print(*data.readlines()[::-1], sep='')