import builtins
from collections import ChainMap, Counter

pylookup = ChainMap(locals(), globals(), vars(builtins))
# print(pylookup)

ct = Counter('abracadabra')
print(ct)
ct.update('aaaaazzz')
print(ct)