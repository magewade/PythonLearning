# numbers = [i for i in input().split(" ")]
# num_set = set()
# len_set = 0
# for i in numbers:
#     num_set.add(int(i))
#     if len(num_set) > len_set:
#         len_set = len(num_set)
#         print("NO")
#     else:
#         print("YES")
#

numbers = [int(i) for i in input().split()]
myset = set()

for i in numbers:
    if i in myset:
        print('YES')
    else:
        print('NO')
        myset.add(i)