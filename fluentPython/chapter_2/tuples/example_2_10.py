# A named tuple type has a few attributes in addition to those inherited from tuple .
# Example 2-10 shows the most useful: the _fields class attribute, the class method
# _make(iterable) and the _asdict() instance method.

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
Latlong = namedtuple('Latlong', 'lat long')
delhi_dat = ('Delhi NCR', 'IN', 21.935, Latlong(28.613889, 77.208889))
delhi = City._make(delhi_dat)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(f"{key}: {value}")


# _fields is a tuple with the field names of the class.
# _make() lets you instantiate a named tuple from an iterable; City(*delhi_da
# ta) would do the same.
# _asdict() returns a collections.OrderedDict built from the named tuple
# instance. That can be used to produce a nice display of city data.