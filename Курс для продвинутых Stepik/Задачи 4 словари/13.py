n = int(input())
words = [input().split() for _ in range(n)]

words_1 = {}
words_2 = {}

for word, synonim in words:
    words_1[word] = synonim
    words_2[synonim] = word

word_input = input()
print(words_1.get(word_input, ''), words_2.get(word_input, ''), sep='')
