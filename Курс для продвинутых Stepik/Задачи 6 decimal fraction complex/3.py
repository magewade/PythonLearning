import fractions
import math

n = int(input())
up = n // 2
down = n - up
results = []
while up != 0:
    if math.gcd(up, down) == 1:
        results.append(fractions.Fraction(f'{str(up)}/{str(down)}'))
    up -= 1
    down += 1
print(max(results))