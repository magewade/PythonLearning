import random

people = [input() for _ in range(int(input()))]
friends = {}
for man in people:
    friends.setdefault(man)

while None in friends.values():
    random.shuffle(people)
    for man in people:
        for key, value in friends.items():
            if man != key and man not in friends.values() and value == None:
                friends[key] = man
                people.remove(man)
            continue

for key, value in friends.items():
    print(f"{key} - {value}")