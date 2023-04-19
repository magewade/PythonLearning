# num_of = input()
# refrigerator = []
# counter = 0
# for i in range(int(num_of)):
#     refrigerator.append(input())
#
#
# def anton(refriger):
#     anton_set = ['a', 'n', 't', 'o', 'n']
#     anton_word = ""
#     list_refriger = list(refriger)
#     for k in list_refriger:
#         if k in anton_set:
#             if k == 'a' and len(anton_set) == 5:
#                 anton_set.remove(k)
#                 anton_word += k
#             elif k == 'n' and len(anton_set) == 4:
#                 anton_set.remove(k)
#                 anton_word += k
#             elif k == 't' and len(anton_set) == 3:
#                 anton_set.remove(k)
#                 anton_word += k
#             elif k == 'o' and len(anton_set) == 2:
#                 anton_set.remove(k)
#                 anton_word += k
#             elif k == 'n' and len(anton_set) == 1:
#                 anton_set.remove(k)
#                 anton_word += k
#
#     print(anton_word)
#     if not anton_set and anton_word == "anton":
#         return True
#
#
# answer = ""
# for i in refrigerator:
#     if anton(i):
#         answer += str(refrigerator.index(i) + 1) + " "
#
#
# print(answer)


for i in range(int(input())):
    s, virus, x = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break
