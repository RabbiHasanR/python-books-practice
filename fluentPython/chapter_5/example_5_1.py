# Create and test a function, then read its __doc__ and check its type.

def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

# print(factorial(42))
# print(factorial.__doc__)
# print(type(factorial))
# print(help(factorial))