n = int(input())
m = int(input())
books = [input() for _ in range(n)]
library = [input() for _ in range(m)]
for book in library:
    print("YES") if book in books else print("NO")


m, n = int(input()), int(input())
libr = {input() for _ in range(m)}

for _ in range(n):
    if input() in libr:
        print('YES')
    else:
        print('NO')




# print("OK" if len(city_list) == len(set(city_list)) else "REPEAT")