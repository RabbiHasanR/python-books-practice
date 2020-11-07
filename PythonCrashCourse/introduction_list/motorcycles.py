motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'Gixxer')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

popped_with_position_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_with_position_motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
