n, m = input().split()
field = [['*' for _ in range(int(m))] for _ in range(int(n))]

for i in range(int(n)):
    for j in range(int(m)):
        if (i + j) % 2 == 0:
            field[i][j] = '.'


for row in field:
    print(*row)