square = input()
matrix = [["."] * 8 for _ in range(8)]
field = [["."] * 8 for _ in range(8)]
elem, row = 0, 0

for i in list('87654321'):
    for j in list("abcdefgh"):
        field[elem][row] = j + i
        row += 1
    elem += 1
    row = 0

for i in range(8):
    for j in range(8):
        if field[i][j] == square:
            matrix[i][j] = "N"
            square_x = i
            square_y = j

for i in range(8):
    for j in range(8):
        if (square_x - i) * (square_y - j) == 2 or (square_x - i) * (square_y - j) == -2:
            matrix[i][j] = "*"

for row in matrix:
    print(*row)
