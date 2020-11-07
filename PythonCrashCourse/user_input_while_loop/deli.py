sandwich_orders = ['Chicken Sandwich', 'pastrami', 'Fish Sandwich', 'Fried Egg Sandwich', 'pastrami', 'Grilled Cheese Sandwich', 'pastrami']
finished_sandwiches = []

print('the deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

index = 0
while index < len(sandwich_orders):
    print(f"I made your {sandwich_orders[index]}")
    finished_sandwiches.append(sandwich_orders[index])
    
    index += 1


print('\n All finished sandwiches:')
for finished_sandwiche in finished_sandwiches:
    print(f"\t{finished_sandwiche}")