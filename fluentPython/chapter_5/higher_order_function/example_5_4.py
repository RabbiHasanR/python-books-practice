# Sorting a list of words by their reversed spelling.

def reverse(word):
    return word[::-1]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=reverse))