# total = 0
# my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]
#
# for li in my_list:
#     total += len(li)
#
# print(total)
#
#
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(700)
#
# print(list1)
#
#
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if list1[i][j] > maximum:
#             maximum = list1[i][j]
# print(maximum)
#
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in range(len(list1)):
#     list1[i].reverse()
#
# print(list1)

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in range(len(list1)):
    counter += len(list1[i])
    for j in range(len(list1[i])):
        total += list1[i][j]
print(total)
print(counter)
print(total/counter)