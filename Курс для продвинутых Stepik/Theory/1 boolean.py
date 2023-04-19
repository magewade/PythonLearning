def func(num1, num2):
    if num1 % num2 != 0:
        return False
    else:
        return True


n1, n2 = int(input()), int(input())
if func(n1, n2):
    print("делится")
else:
    print("не делится")
