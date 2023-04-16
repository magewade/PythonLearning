# result = {i: i ** 2 for i in range(1, 16)}
# print(result)


dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
for element in dict1:
    for item in dict2:
        if item == element:
            dict1[element] += dict2[item]

dict2.update(dict1)
result = dict2.copy()
print(result)


result = dict1.copy()
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value