from functools import reduce

with open("nums.txt") as nums:
    result = []
    result_2 = ""
    for line in nums:
        result.append(list(map(lambda x: x if x.isdigit() else "*", line)))

    for i in result:
        for j in i:
            if j == "*":
                result_2 += " "
            else:
                result_2 += j

    print(reduce(lambda x, y: int(x) + int(y), result_2.strip().split()))

    with open('nums.txt') as file:
        temp = ''
        n = 0
        for c in file.read():
            if c.isdigit():
                temp += c
            elif temp != '':
                n += int(temp)
                temp = ''
        print(n)
