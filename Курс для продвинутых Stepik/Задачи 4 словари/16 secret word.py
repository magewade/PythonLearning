cipher = input()
alpabet = {}

for i in range(int(input())):
    letter, amount = input().split(': ')
    alpabet.update(alpabet.fromkeys(letter, amount))

for let in cipher:
    for key, value in alpabet.items():
        if str(cipher.count(let)) == value:
            print(key, end='')

