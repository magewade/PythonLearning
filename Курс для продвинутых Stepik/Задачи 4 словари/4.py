dict = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}

input_str = list(input())
count = 0
for litera in input_str:
    for key, value in dict.items():
        if litera.upper() in value:
            count += 1
            print(key * (value.index(litera.upper()) + 1), end='')