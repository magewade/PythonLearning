points = int(input())
ox_i = 0
ox_ii = 0
ox_iii = 0
ox_iv = 0
for i in range(points):
    point = input()
    ox = point.split(" ")
    if int(ox[0]) > 0 and int(ox[1]) > 0:
        ox_i += 1
    elif int(ox[0]) > 0 and int(ox[1]) < 0:
        ox_iv += 1
    elif int(ox[0]) < 0 and int(ox[1]) < 0:
        ox_iii += 1
    elif int(ox[0]) < 0 and int(ox[1]) > 0:
        ox_ii += 1
    else:
        continue
print(f"Первая четверть: {ox_i}")
print(f"Вторая четверть: {ox_ii}")
print(f"Третья четверть: {ox_iii}")
print(f"Четвертая четверть: {ox_iv}")
