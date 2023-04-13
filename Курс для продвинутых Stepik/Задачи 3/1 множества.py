numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
sort_numbers = sorted(numbers, reverse=True)
# print(*sort_numbers, sep='\n')

set1, set2, set3 = input().split()
print(("NO", "YES")[set(set1) == set(set2) == set(set3)])


myset = set()
for i in range(10):
    if i % 2 == 0:
        myset.add('even')
    else:
        myset.add('odd')
print(len(myset))