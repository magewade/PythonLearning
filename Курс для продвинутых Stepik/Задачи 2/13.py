# a, b, c = int(input()), int(input()), int(input())
# result = (-b/(2*a), (4*a*c - b**2)/(4*a))
# print(result)


# n = int(input())
# students = tuple([input() for i in range(n)])
# print(*students, sep='\n')
# print()
# for student in students:
#     if "5" in student:
#         print(student)
#     elif "4" in student:
#         print(student)

students = [tuple(input().split()) for _ in range(int(input()))]
print(students)

for student in students:
    print(*student)

print()

for name, grade in students:
    if int(grade) > 3:
        print(name, grade)