# n, m = int(input()), int(input())
# mult = []
#
# def print_matrix(matrix, n, m, width=3):
#     for r in range(n):
#         for c in range(m):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
# mult_ready = []
# for i in range(n):
#     for j in range(m):
#         temp = i * j
#         mult.append(temp)
#     row = mult[i * m:(i + 1) * m]
#     mult_ready.append(row)
#
#
# print_matrix(mult_ready, n, m)


n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()