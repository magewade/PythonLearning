s = [input() for _ in range(int(input()))]
count = 0
word = list(s[0])
pref = ''
flag = True
for letter in word:
    pref += letter
    for elem in s:
        if pref not in elem:
            flag = False
            break
    if flag == False:
        pref = pref[:-1]
        break

if pref == '':
    print("nan")
else:
    print(pref)
