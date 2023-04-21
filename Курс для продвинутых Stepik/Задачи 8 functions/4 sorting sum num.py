def comparator(n):
    return sum([int(i) for i in str(n)])


numbers = [int(i) for i in input().split()]

numbers.sort()
print(*sorted(numbers, key=comparator))

