n, m = int(input()), int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

maximum = matrix[0][0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

for i in range(len(matrix)):
    try:
        j = matrix[i].index(maximum)
        print(i, j)
        break
    except ValueError:
        pass




