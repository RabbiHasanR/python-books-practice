from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

with open('floats.bin', 'wb') as fp:
    floats.tofile(fp)

floats2 = array('d')
with open('floats.bin', 'rb') as fp:
    floats2.fromfile(fp, 10**7)

print(floats2[-1])

print(floats2 == floats)