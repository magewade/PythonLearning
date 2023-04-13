print(("YES", "NO")[set(input()).isdisjoint(set(input()))])

print('NO' if set(input()).isdisjoint(set(input())) else 'YES')

print('YES' if set(input()).issuperset(set(input())) else 'NO')

student_1 = set([int(i) for i in input().split()])
student_2 = set([int(i) for i in input().split()])
student_3 = set([int(i) for i in input().split()])
print(*sorted((student_1 & student_2) - student_3, reverse=True))