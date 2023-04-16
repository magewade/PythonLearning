city_list = [input().split() for _ in range(int(input()))]
cities = [input().split() for _ in range(int(input()))]
city_dict = {}

for element in city_list:
    city_dict[element[0]] = element[1:]

for city in cities:
    for key, value in city_dict.items():
        if city[0] in value:
            print(key)


d = {}
for _ in range(int(input())):
    country, *cities = input().split()
    d.update(dict.fromkeys(cities, country))
for _ in range(int(input())):
    print(d[input()])
