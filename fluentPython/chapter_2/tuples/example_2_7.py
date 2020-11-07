import os

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# tuple unpacking
lattitude, longitude = lax_coordinates
print(lattitude)
print(longitude)

# swaping example with tuple unpacking
a = 1
b = 2

a, b = b, a
print(a, b)

# Latitude and longitude of the Los Angeles International Airport.
# Data about Tokyo: name, year, population (millions), population change (%),
# area (km2).
# A list of tuples of the form (country_code, passport_number).
# As we iterate over the list, passport is bound to each tuple.
# The % formatting operator understands tuples and treats each item as a separate
# field.
# The for loop knows how to retrieve the items of a tuple separately — this is
# called “unpacking”. Here we are not interested in the second item, so it’s assigned
# to _ , a dummy variable.


# the
# os.path.split() function builds a tuple (path, last_part) from a filesystem path.

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename) 

# using starred * for tuple unpacking

a, b, *rest = range(5)
print(a, b, rest)


# In the context of parallel assignment, the * prefix can be applied to exactly one variable,
# but it can appear in any position:

a, b, *rest, c, d = range(10)
print(a, b, rest, c , d)

*head, b, c, d = range(5)
print(head, b, c, d)
