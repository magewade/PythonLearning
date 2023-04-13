# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three,
# and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and
# dells of memory, over which, if you can still stand my style (I am writing under observation), the sun
# of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges,
# about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill,
# in the summer dusk; a furry warmth, golden midges.'''
# words = {i.strip(':,.!?();').lower() for i in sentence.split() if len(i.strip(':,.!?();')) < 4}
# print(*sorted(words))


# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# print(*sorted({png.lower() for png in files if ".png" in png.lower()}))

a = {'a', 'b', 'c', 'd', 'e'}
b = {'b', 'c', 'd'}
c = a + b
print(c)