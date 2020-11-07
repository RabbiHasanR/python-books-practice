# Using memoryview and struct to inspect a GIF image header.
import struct

fmt = '<3s3sHH'

with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(header)
print(bytes(header))

img_tupels = struct.unpack(fmt, header)
print(img_tupels)
del header
del img
