# z1, z2 = complex(input()), complex(input())
# print(f"{str(z1)} + {str(z2)} = {z1 + z2}")
# print(f"{str(z1)} - {str(z2)} = {z1 - z2}")
# print(f"{str(z1)} * {str(z2)} = {z1 * z2}")

n = int(input())
z1, z2 = complex(input()), complex(input())
print(z1**n + z2**n + (z1.conjugate())**n + (z2.conjugate())**(n + 1))