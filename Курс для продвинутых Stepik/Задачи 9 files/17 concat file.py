n = int(input())
with open('output', 'w') as output:
    for i in range(n):
        name = input()
        with open(name, 'r') as inp:
            content = inp.read()
        output.write(content)

