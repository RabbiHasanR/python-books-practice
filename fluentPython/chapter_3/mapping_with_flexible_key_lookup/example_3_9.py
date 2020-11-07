# MappingProxyType builds a read-only mappingproxy instance from a
# dict .

from types import MappingProxyType

d = {1: 'A'}

d_proxy = MappingProxyType(d)

print(d_proxy)
print(d_proxy[1])
d_proxy[2] = 'x'
print(d_proxy)

