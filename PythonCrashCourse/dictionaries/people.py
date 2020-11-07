person_0 = {
    'first_name': 'rabbi',
    'last_name': 'hasan',
    'age': 25,
    'country': 'bangladesh'
    }

person_1 = {
    'first_name': 'ziaul',
    'last_name': 'piash',
    'age': 25,
    'country': 'india'
    }

people = [person_0, person_1]
for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"Full name: {full_name}, Age: {person['age']}, Country: {person['country'].title()}")
