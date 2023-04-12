n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            print("NO")
            exit()

print("YES")

