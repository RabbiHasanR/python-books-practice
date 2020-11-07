cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

sorted_cars = sorted(cars)
print('Original list: ', cars)
print('Sorted list: ', sorted_cars)
print('Original list again: ', cars)

cars.reverse()
print(cars)
print(len(cars))