# Initializing bytes from the raw data of an array .
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
octets = bytes(numbers)
print(octets)
octets_arr = bytearray(numbers)
print(octets_arr)