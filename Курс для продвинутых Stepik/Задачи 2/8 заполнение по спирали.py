n, m = input().split()
n, m = int(n), int(m)

matrix = [[0] * m for _ in range(n)]
num = 1
i, j = 0, 0
di, dj = 0, 1

for _ in range(n * m):
    matrix[i][j] = num
    num += 1
    if matrix[(i + di) % n][(j + dj) % m] != 0:
        di, dj = dj, -di
    i, j = i + di, j + dj

for row in matrix:
    print(*row)

# TODO check how it work later
