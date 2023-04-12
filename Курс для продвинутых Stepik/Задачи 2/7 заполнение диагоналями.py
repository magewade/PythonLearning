n, m = input().split()
n, m = int(n), int(m)
matrix = [[1 for _ in range(m)] for _ in range(n)]

num = 0
for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                num += 1
                matrix[i][j] = num

for row in matrix:
    print(*row)