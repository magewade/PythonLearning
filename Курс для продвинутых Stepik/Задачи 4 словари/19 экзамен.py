# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# result = {key: [i for i in value if i <= 20] for key, value in my_dict.items()}
# print(result)

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
# result = []
#
# for key, value in emails.items():
#     for name in value:
#         result.append(name + "@" + key)
#
# print(*sorted(result), sep="\n")

# str_input = input().split()
# result = {}
# for lit in str_input:
#     if lit in result:
#         print(f'{result[lit]}', end=' ')
#     else:
#         print(1, end=' ')
#     result[lit] = result.get(lit, 1) + 1
# TODO: figure out

# def build_query_string(params):
#     result = []
#     for key, value in params.items():
#         result.append(key + "=" + str(value))
#     result.sort()
#     result = "&".join(result)
#     return result
#
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
#
# def build_query_string(params):
#     res = [f'{k}={v}' for k, v in params.items()]
#     return '&'.join(sorted(res))
# TODO figure out

# def merge(values):
#     result = {}
#     for dct in values:
#         for key, value in dct.items():
#             result.setdefault(key, set()).add(value)
#     return result
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# # result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
# print(result)

# TODO разобраться с дурацким сетдефолт

# transform = {'execute': 'X', 'write': 'W', 'read': 'R'}
# mydict = {}
#
# for _ in range(int(input())):
#     name, *operations = input().split()
#     mydict[name] = operations
#
# for _ in range(int(input())):
#     operation, name = input().split()
#     if transform[operation] in mydict[name]:
#         print('OK')
#     else:
#         print('Access denied')


n = int(input())
people = {}
for i in range(n):
    line = input().split()
    if line[0] not in people.keys():
        people[line[0]] = people.setdefault(line[0], {line[1]: int(line[2])})
    else:
        if line[1] not in people[line[0]]:
            people[line[0]].update({line[1]: int(line[2])})
        else:
            people[line[0]][line[1]] += int(line[2])
people = dict(sorted(people.items()))

for name, list in people.items():
    list = dict(sorted(list.items()))
    print(f'{name}:')
    for item, number in list.items():
        print(f'{item} {number}')
