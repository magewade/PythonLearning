# set_1 = [i for i in input().split()]
# set_2 = [i for i in input().split()]
# print(len(set(set_1)&set(set_2)))
from unittest import result

# set_1 = [int(i) for i in input().split()]
# set_2 = [int(i) for i in input().split()]
# print(*(sorted(set(set_1)&set(set_2))))


# set_1 = [int(i) for i in input().split()]
# set_2 = [int(i) for i in input().split()]
# print(*(sorted(set(set_1)-set(set_2))))


n = int(input())
numbers = []
for i in range(n):
    numbers.append(input())
inter_results = set(numbers[0])
for number in numbers:
    inter_results &= set(number)
print(*sorted(inter_results))

n = int(input())
numbers = [input() for _ in range(n)]
num_set = set(numbers[0]).intersection(*numbers)
print(*sorted(num_set))

