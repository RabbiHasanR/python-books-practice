tt = (1, 2, (30, 40))
print(hash(tt))

tl = (1, 2, [30, 40])
# print(hash(tl)) # TypeError: unhashable type: 'list'

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))