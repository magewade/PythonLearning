import math

n = int(input())
amebs = 1
iter = math.floor(n / 3)
while iter > 0:
    amebs *= 2
    iter -= 1
print(amebs)
