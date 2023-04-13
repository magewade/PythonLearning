words = input().lower().split()
new_words = []
for word in words:
    new_words.append(word.strip('.,;:-?!'))
print(len(set(new_words)))
