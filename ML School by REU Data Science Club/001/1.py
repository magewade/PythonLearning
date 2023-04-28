s = [int(input()) for i in range(int(input()))]
target = int(input())
for i in s:
    if (target - i) in s and s.index(target - i) != s.index(i):
        print(s.index(i), s.index(target - i))
        break