num = input()
num2 = num[::-1]
num3 = ""
for i in range(0, len(num2), 3):
    num3 = num3 + num2[i:i+3] + ","
num4 = num3[::-1]
print(num4[1::])

