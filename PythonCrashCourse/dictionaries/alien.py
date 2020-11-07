alien_0 = {'color': 'green', 'point': 5}

print(alien_0['color'])
print(alien_0['point'])
print(alien_0)

# alien_0 = {'color': 'red'}

# print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position {alien_1['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_1['speed'] == 'slow':
    x_increament = 1
elif alien_1['speed'] == 'medium':
    x_increament = 2
else:
    x_increament = 3

# The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increament

print(f"New position {alien_1['x_position']}")


del alien_0['point']
print(alien_0)