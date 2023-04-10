# elem = int(input())
# row = int(input())
# words = my_list = [[0 for j in range(row)] for i in range(elem)]
# r, e = 0, 0
# counter = elem * row + row + 1
# if elem == 1 or row == 1:
#     counter = elem * row + elem + 1
# for i in range(counter):
#     if r < row and e < elem:
#         words[e][r] = input()
#         r += 1
#     elif e < elem:
#         e += 1
#         r = 0
#
#
# for row in words:
#     for elem in row:
#         print(elem, end=' ')
#     print()



n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print()

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()