


s = "afbjabbbbbababa"
s = list(s)
counter = 0
mark = False
i = 0
while i < len(s):
    if s[i] == "a":
        c = s[i:]
        s.remove("a")
        i -= 1   # reset i to previous index position
        for j in c:
            if j == "b":
                counter += 1
    i += 1   # increment i at the end of each iteration

print(counter)