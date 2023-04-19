n, m = int(input()), int(input())    # считываем значения n и m
my_list = [[0] * m for _ in range(n)]
print(my_list)


n = 4                                          # количество строк (элементов)
my_list = []
for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    my_list.append(elem)


my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')   # используем необязательный параметр end
    print()                             # перенос на новую строку


for row in my_list:
    for elem in row:
        print(elem, end=' ')
    print()


my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
total = 0
for row in my_list:
    for elem in row:
        total += elem
print(total)


total = 0
for row in my_list:      # в один цикл
    total += sum(row)
print(total)