n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
temp = matrix.copy
result = matrix.copy()


def power(matrix_1, matrix_2, n, l, k):
    res = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            for y in range(k):
                res[i][j] += matrix_1[i][y] * matrix_2[y][j]
    return res


for i in range(m - 1):
    temp = power(result, matrix, n, n, n)
    result = temp

for row in result:
    print(*row)
