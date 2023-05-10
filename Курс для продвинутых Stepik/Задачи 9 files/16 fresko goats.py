with open('/Users/magewade/Desktop/Python/Курс для продвинутых Stepik/Задачи 9 files/goats.txt', 'r') as f:
    lines = f.readlines()

colors = []
for i in range(1, lines.index('GOATS\n')):
    colors.append(lines[i].strip())

goats = lines[lines.index('GOATS\n') + 1:]
total_goats = len(goats)

color_counts = {}
for color in colors:
    color_counts[color] = goats.count(color + '\n')

selected_colors = []
for color in colors:
    if color_counts[color] / total_goats > 0.07:
        selected_colors.append(color)

selected_colors.sort()

with open('answer.txt', 'w') as f:
    for color in selected_colors:
        f.write(color + '\n')
