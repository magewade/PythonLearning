n, m = input().split()
n, m = int(n), int(m)
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
input()
k, l = input().split()
k, l = int(k), int(l)
matrix_2 = [[int(i) for i in input().split()] for _ in range(k)]

multip = [[0] * l for _ in range(n)]

for i in range(n):
    for j in range(l):
        for y in range(k):
            multip[i][j] += matrix_1[i][y] * matrix_2[y][j]


for row in multip:
    print(*row)