s = input()
lst = s.split()

res = [[]]
for i in lst:
    res.append([i])

for i in range(2, len(lst) + 1):
    for j in range(len(lst) - i + 1):
        res.append(lst[j:j + i])

sorted_list = [[]]
for i in range(1, len(lst) + 1):
    for j in res:
        if len(j) == i:
            sorted_list.append(j)

print(sorted_list)
