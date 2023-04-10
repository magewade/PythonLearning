n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]



def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = n * (n ** 2 + 1) // 2
    numbers = [i for i in range(1, n**2 + 1)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] in numbers:
                numbers.remove(matrix[i][j])

    if numbers:
        return False


    for i in range(n):
        if sum(matrix[i]) != magic_sum:
            return False
        if sum(matrix[j][i] for j in range(n)) != magic_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(matrix[i][n - i - 1] for i in range(n)) != magic_sum:
        return False

    return True


if is_magic_square(matrix):
    print("YES")
else:
    print("NO")