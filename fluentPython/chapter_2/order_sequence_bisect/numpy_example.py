# NumPy also supports high-level operations for loading, saving and operating on all
# elements of a numpy.ndarray .

import numpy
from array import array
from random import random

# floats = list((random() for i in range(10**7)))
# print(floats[-1])

# with open('floats-10M-lines.txt', 'w') as fp:
#     for item in floats:
#         fp.write(str(item))


floats = numpy.loadtxt('floats-10M-lines.txt')
print(len(floats))