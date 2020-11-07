# Factorial implemented with reduce and an anonymous function.
from functools import reduce

def fact(n):
    return reduce(lambda a, b: a * b, range(1, n+1))

print(fact(5))


# Factorial implemented with reduce and operator.mul .
from operator import mul

def fact_2(n):
    return reduce(mul, range(1, n+1))

print(fact(5))