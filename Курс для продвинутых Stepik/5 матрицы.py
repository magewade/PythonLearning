matrix = [[2, -5, -11, 0],
           [-9, 4, 6, 13],
           [4, 7, 12, -2]]

print(matrix[1][2])  # вывод элемента на позиции (2, 3)


rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
matrix = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()


rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()


n = 8
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8

for i in range(n):                     # заполняем главную диагональ единицами, а побочную двойками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2

for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()


def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)