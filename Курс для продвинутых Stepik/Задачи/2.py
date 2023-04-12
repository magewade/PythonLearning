num = input()
if len(num) == 5:
    print(int(num[::-1]))
else:
    print(num[0], num[:-6:-1], sep="")
