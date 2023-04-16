s1 = [i for i in input().lower() if i.isalpha()]
s2 = [i for i in input().lower() if i.isalpha()]
print('YES' if sorted(s1) == sorted(s2) else 'NO')
