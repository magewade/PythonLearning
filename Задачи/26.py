n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
rows = input().split()
i = int(rows[0])
j = int(rows[1])
print(i)


print(matrix)

for k in range(n):
    matrix[k][i-1], matrix[k][j-1] = matrix[k][j-1], matrix[k][i-1]

for row in matrix:
    print(*row)
