numb = int(input())
numb_bin = bin(numb)[2:]
pos_bin = numb_bin[1:] + numb_bin[0]
print(pos_bin)
pos = int(pos_bin, 2)
print(pos)