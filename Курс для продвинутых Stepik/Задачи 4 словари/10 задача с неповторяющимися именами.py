# s = input().split(' ')
# result = {}
# for items in s:
#     result[items] = result.get(items, 0) + 1
#
# printer = ''
# count = 1
# counter = {}
# for item in s:
#     if result.get(item) == 1:
#         printer += item + " "
#     else:
#         if item in printer:
#             printer += item + "_" + str(counter[item][1]) + " "
#             counter[item][1] += 1
#         else:
#             counter[item] = [result[item], 1]
#             printer += item + " "
#
# print(printer)



lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{c}_{res[c]}', end=' ')
    else:
        print(c, end=' ')
    res[c] = res.get(c, 0) + 1