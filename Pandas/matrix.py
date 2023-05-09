import numpy as np
a = np.array([[9.8, 2., 3., 4.], [0., 7.4, -1., 1.], [0., 0., 1., 1.], [0., 0., -1., 1.]])
b = np.array([1., 1., 0., 2.])


print(a, b)
result = np.linalg.solve(a, b)
print(result)


# ввод из строи, содержащих три положительных числа
n1, n2, n3 = input(), input(), input()

# ДАЛЕЕ КОД СТУДЕНТА...
nums = sorted([round(float(n1)), round(float(n2)), round(float(n3))])

result = ', '.join(str(num) for num in nums)

print(result)