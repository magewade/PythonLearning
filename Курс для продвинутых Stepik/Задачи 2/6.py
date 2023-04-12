n, m = input().split()
n, m = int(n), int(m)
matrix = [[1 for _ in range(m)] for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = num
        num += 1

counter = 0
for row in matrix:
    if (counter + 1) % 2 == 0:
        row.reverse()
    counter += 1

for row in matrix:
    print(*row)
