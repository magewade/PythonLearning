ea_string = input()
ea_list = list(ea_string)
max_count = 0
count = 0
flag = False
for i in ea_list:
    if i == "Р":
        count += 1
        flag = True
    else:
        flag = False
        if count > max_count:
            max_count = count
        count = 0
if count > max_count:
    max_count = count
print(max_count)
