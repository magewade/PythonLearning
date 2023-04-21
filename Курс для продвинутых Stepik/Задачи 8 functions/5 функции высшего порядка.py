def predicate(word):
    return word == word[::-1]


words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
result = filter(predicate, words)
print(*result)