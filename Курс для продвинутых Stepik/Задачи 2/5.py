# n = int(input())
# matrix = [[0 for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j + 1 == n:
#             matrix[i][j] = 1
#
# for row in matrix:
#     print(*row)


n = int(input())

matrix = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]

for row in matrix:
    print(*row)