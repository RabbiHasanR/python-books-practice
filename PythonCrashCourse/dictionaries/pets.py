cat = {'kind_of_animal': 'pet type', 'owner': 'rabbi'}
dog =  {'kind_of_animal': 'pet type', 'owner': 'piash'}
tiger =  {'kind_of_animal': 'wild type', 'owner': 'borna'}

pets = [cat, dog, tiger]
for pet in pets:
    print(f"Animal type: {pet['kind_of_animal']} Owner: {pet['owner']}")
    