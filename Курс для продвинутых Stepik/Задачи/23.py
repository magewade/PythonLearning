n = int(input())
matrix = []
step = 0
counter = 0
j = 0
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

up = 0
down = 0
left = 0
right = 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            up += matrix[i][j]
        elif j > i > n - 1 - j:
            right += matrix[i][j]
        elif i > j and i > n - 1 - j:
            down += matrix[i][j]
        elif j < i < n - 1 - j:
            left += matrix[i][j]

print("Верхняя четверть:", up)
print("Правая четверть:", right)
print("Нижняя четверть:", down)
print("Левая четверть", left)
