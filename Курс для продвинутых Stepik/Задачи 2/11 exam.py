# line = [i for i in input().split()]
# n = int(input())
#
# step = len(line) // n
# result = []
# counter = 0
# for j in range(0, len(line), step):
#     for i in range(counter, len(line), n):
#         result.append(line[i])
#     result.append("STOP")
#     counter += 1
#
# end_result = []
# temp = []
# counter = 0
#
# for i in range(len(result)):
#     if counter == n:
#         break
#     elif result[i] != "STOP":
#         temp.append(result[i])
#     else:
#         counter += 1
#         end_result.append(temp)
#         temp = []
#
# print(end_result)


# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)



# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# maximum = matrix[n - 1][n - 1]
#
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] > maximum and (i >= n - 1 - j):
#             maximum = matrix[i][j]
#
# print(maximum)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[j][i], end=" ")
#     print()


# n = int(input())
# snow = [["."] * n for _ in range(n)]
# print(snow)
# for i in range(n):
#     for j in range(n):
#         if i == j or j == n - 1 - i or i == n//2 or j == n//2:
#             snow[i][j] = "*"
#
# for row in snow:
#     print(*row)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
# flag = True
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[n-1-j][n-1-i]:
#             flag = False
#             break
#     if not flag:
#         break
#
# if flag:
#     print("YES")
# else:
#     print("NO")


# square = input()
# matrix = [["."] * 8 for _ in range(8)]
# field = [["."] * 8 for _ in range(8)]
# elem, row = 0, 0
#
# for i in list('87654321'):
#     for j in list("abcdefgh"):
#         field[elem][row] = j + i
#         row += 1
#     elem += 1
#     row = 0
#
# for i in range(8):
#     for j in range(8):
#         if field[i][j] == square:
#             matrix[i][j] = "N"
#             square_x = i
#             square_y = j
#
# for i in range(8):
#     for j in range(8):
#         if abs(square_x - i) == abs(square_y - j) or square_x == i or square_y == j:
#             matrix[i][j] = "*"
#
# for i in range(8):
#     for j in range(8):
#         if field[i][j] == square:
#             matrix[i][j] = "Q"
#             square_x = i
#             square_y = j
#
# for row in matrix:
#     print(*row)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
#
# def is_latin_square(matrix, n):
#     for row in matrix:
#         if len(set(row)) != n or set(row) != set(range(1, n+1)):
#             return False
#
#     for j in range(n):
#         column = {matrix[i][j] for i in range(n)}
#         if len(column) != n or set(column) != set(range(1, n+1)):
#             return False
#
#     return True
#
#
# if is_latin_square(matrix, n):
#     print("YES")
# else:
#     print("NO")


n = int(input())
matrix = [[0] * n for i in range(n)]


for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)

for row in matrix:
    print(*row)