from random import sample

numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()