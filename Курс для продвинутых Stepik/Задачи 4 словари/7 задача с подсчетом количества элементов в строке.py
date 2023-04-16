text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
print(text)
result = {}
for num in text:
    result[num] = result.get(num, 0) + 1
print(result)
