input_string = input().split(" ")
result = []

i = 0
while i < len(input_string):
    current_char = input_string[i]
    count = 1
    while i + count < len(input_string) and input_string[i + count] == current_char:
        count += 1
    if count > 1:
        result.append([current_char] * count)
        i += count
    else:
        result.append([current_char])
        i += 1

print(result)
