dct = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    dct.setdefault(name, []).append(phone)

print(dct)

for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))
