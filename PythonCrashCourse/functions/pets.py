def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type} name is {pet_name.title()}")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='dog', pet_name='willie')

describe_pet(pet_name='willie')