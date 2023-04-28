s = input()
print(('NO', 'YES')[len(s) >= 7 and s.upper() != s and s.lower() != s and any(
    map(lambda x: True if x in '0123456789' else False, s))])
