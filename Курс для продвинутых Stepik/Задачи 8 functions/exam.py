# def concat(*args, sep=" "):
#     result = ''
#     for arg in args:
#         result += str(arg) + sep
#     return result.rstrip(sep)
#
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


# from functools import reduce
#
#
# def product_of_odds(data):   # data - список целых чисел
#     return reduce(lambda x, y: x * y, filter(lambda x: x % 2, data), 1)


# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
#            (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
# sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)
#
# print(sorted_numbers)


# def arithmetic_operation(operation):
#     operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
#     return operations[operation]
#
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))
#
# def gematria(word):
#     result = 0
#     for letter in word.upper():
#         result += ord(letter) - ord("A")
#     return result
#
#
# s = [input() for i in range(int(input()))]
# s.sort()
# print(*sorted(s, key=lambda x: gematria(x)), sep="\n")

s = [input() for i in range(int(input()))]
def sor(ip):
    ip_set = ip.split(".")
    counter = 3
    result = 0
    for i in ip_set:
        result += int(i) * 256**counter
        counter -= 1
    return result
print(*sorted(s, key=lambda x: sor(x)), sep="\n")
