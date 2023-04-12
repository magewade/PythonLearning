# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# def rotate_matrix(matrix):
#     n = len(matrix)
#     for i in range(n // 2):
#         for j in range(i, n - i - 1):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[n - j - 1][i]
#             matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
#             matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
#             matrix[j][n - i - 1] = temp
#     return matrix
#
# matrix = rotate_matrix(matrix)
#
# for row in matrix:
#     print(*row)



n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[i][j] = matrix[n - j - 1][i]

for row in result:
    print(*row)