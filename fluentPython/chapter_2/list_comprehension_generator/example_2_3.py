symbols = '$¢£¥€¤'
# using list comprehension
beyond_ascii = [ord(code) for code in symbols if ord(code) > 127]
print(beyond_ascii)

# using filter and map
beyond_ascii = list(filter(lambda x: x > 127, map(ord, symbols)))
print(beyond_ascii)