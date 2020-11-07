from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(tokyo._fields)
print(City._fields)


# Two parameters are required to create a named tuple: a class name and a list of
# field names, which can be given as an iterable of strings or as a single space-
# delimited string.
# Data must be passed as positional arguments to the constructor (in contrast, the
# tuple constructor takes a single iterable).
# You can access the fields by name or position.