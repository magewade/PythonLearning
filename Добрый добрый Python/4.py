names = list(map(str, input().split()))
counter = 0
flag = False
while counter < len(names):
    if names[counter][0].lower() == names[counter][-1].lower():
        flag = True
        break
    counter += 1

if flag:
    print("ДА")
else:
    print("НЕТ")
