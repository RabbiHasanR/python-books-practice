# Use function through a different name, and pass function as argument.
from example_5_1 import factorial

fact = factorial
print(fact)
print(fact(5))

map_fact = map(fact, range(11))
print(map_fact)

print(list(map_fact))