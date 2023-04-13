# first = {int(i) for i in input().split(" ")}
# second = {int(i) for i in input().split(" ")}
# print("YES") if first == second else print("NO")

# m, n = int(input()), int(input())
# math = {input() for _ in range(m)}
# inf = {input() for _ in range(n)}
# print(len(math ^ inf)) if len(math ^ inf) > 0 else print("NO")

# director = {i for i in input().split(" ")}
# sec_dir = {i for i in input().split(" ")}
# print(*sorted(director | sec_dir))
#
# m, n = int(input()), int(input())
# math_plus_inf = [input() for _ in range(m + n)]
# math_plus_inf_set = set(math_plus_inf)
# if len(set(math_plus_inf)) == (m + n) / 2:
#     print("NO")
# else:
#     print(len(math_plus_inf) - (len(math_plus_inf) - len(math_plus_inf_set)) * 2)


n = int(input())
students_total = []
temp = set()
for i in range(n):
    m = int(input())
    students = {input() for _ in range(m)}
    temp.update(students)
    students_total.append(students)

for student in students_total:
    temp -= temp.difference(student)

print(*sorted(temp), sep="\n")

n = int(input())
result = {input() for _ in range(int(input()))}
for _ in range(n - 1):
    result &= {input() for _ in range(int(input()))}
print(*sorted(result), sep='\n')

