# numbers = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
#
# for i in list(input()):
#     print(numbers[i], end=" ")


d = {
    "CS101": "CS101: 3004, Хайнс, 8:00",
    "CS102": "CS102: 4501, Альварадо, 9:00",
    "CS103": "CS103: 6755, Рич, 10:00",
    "NT110": "NT110: 1244, Берк, 11:00",
    "CM241": "CM241: 1411, Ли, 13:00"
}

n = input()
for key, value in d.items():
    if key == n:
        print(value)
