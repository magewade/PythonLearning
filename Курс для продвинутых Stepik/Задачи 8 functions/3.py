from math import sin

def math_func(n, f):
    return {'квадрат': n**2, 'куб': n**3, 'корень': n**0.5, 'модуль': abs(n), 'синус': sin(n)}[f]

print(math_func(int(input()), input()))  # число, команда