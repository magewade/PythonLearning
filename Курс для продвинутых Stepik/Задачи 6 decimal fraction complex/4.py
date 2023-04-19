import fractions
import math

n = int(input())
results = []
for up in range(1, n + 1):
    for down in range(2, n + 1):
        if math.gcd(up, down) == 1 and up < down:
            results.append(fractions.Fraction(f'{str(up)}/{str(down)}'))

set(results)
results.sort()

print(*(results), sep="\n")