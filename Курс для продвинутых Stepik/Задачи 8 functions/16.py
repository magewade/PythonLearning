s = [[input().split() for i in range(int(input()))] for _ in range(int(input()))]
result = 0
for i in s:
    result += any(map(lambda x: x[1] == "5", i))
print(("NO", "YES")[result == len(s)])
