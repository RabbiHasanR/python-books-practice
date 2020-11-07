# Sorting a list of words by their reversed spelling using lambda .

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))