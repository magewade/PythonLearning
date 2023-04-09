count = input()
numbers = []
for i in range(int(count)):
    numbers.append(input())
multiply = int(input())
flag = False
for i in numbers:
    for j in numbers:
        if int(i) != int(j) or numbers.count(i) > 1:
            if int(i) * int(j) == multiply:
                flag = True
                break

if flag:
    print("ДА")
else:
    print("НЕТ")

