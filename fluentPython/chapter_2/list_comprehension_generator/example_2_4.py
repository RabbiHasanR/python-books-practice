colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# using list comprehension
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# using for loop
for color in colors:
    for size in sizes:
        print((color, size))