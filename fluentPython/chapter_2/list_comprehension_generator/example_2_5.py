import array

symbols = '$¢£¥€¤'
tuple_result = tuple(ord(code) for code in symbols)
print(tuple_result)

array_result = array.array('I', (ord(code) for code in symbols))
print(array_result)


# If the generator expression is the single argument in a function call, there is no
# need to duplicate the enclosing parenthesis.
# The array constructor takes two arguments, so the parenthesis around the
# generator expression are mandatory 3 .