from collections import Counter

word = '1234512'
c = Counter(word)
print(type(c.most_common(1)[0][0]))