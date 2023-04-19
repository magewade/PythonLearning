num = int(input())
triangle = [1]
counter = 1


def generate_next_string(prev_string):
    next_string = prev_string.copy()
    next_string.append(1)
    index = 1
    for el in prev_string:
        if index == len(prev_string):
            break
        else:
            next_string[index] = prev_string[index - 1] + prev_string[index]
            index += 1
    return next_string


def print_triangle(triangle):
    for row in triangle:
        for elem in row:
            print(elem, end=' ')
        print()



if num == 1:
    print(1)
elif num == 2:
    print(1)
    print(1, 1)
else:
    triangle = [[1], [1, 1]]
    for i in range(2, num):
        triangle.append(generate_next_string(triangle[i - 1]))
    print_triangle(triangle)

