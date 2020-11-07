colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tsirt in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tsirt)


# The generator expression yields items one by one; a list with all 6 t-shirt
# variations is never produced in this example.