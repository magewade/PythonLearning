num_of_people, step = int(input()), int(input())
people, circle = [x for x in range(1, num_of_people + 1)], 0
print(people)
print(circle)
while len(people) > 1:
    circle = (circle + step - 1) % len(people)
    del people[circle]
print(people[0])