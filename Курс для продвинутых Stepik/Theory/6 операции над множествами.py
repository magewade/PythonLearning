# Объединение множеств: метод union()
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1.union(myset2)
print(myset3)

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1 | myset2
print(myset3)

# Пересечение множеств: метод intersection()
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1.intersection(myset2)
print(myset3)

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1 & myset2
print(myset3)

# Разность множеств: метод difference()
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1.difference(myset2)
print(myset3)

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1 - myset2
print(myset3)

# Симметрическая разность: метод symmetric_difference()
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1.symmetric_difference(myset2)
print(myset3)

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1 ^ myset2
print(myset3)