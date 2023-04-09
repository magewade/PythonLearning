n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
rows = input().split()
i = int(rows[0])
j = int(rows[1])


for k in range(n):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]

for row in matrix:
    print(*row)
