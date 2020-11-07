favorite_numbers = {
    'rabbi': [1, 2],
    'piash': [3, 4],
    'tuhin': [5, 6],
    'borna': [7, 8],
    'tasmia': [9, 10],
    }

# print(favorite_numbers['rabbi'])
# print(favorite_numbers['piash'])
# print(favorite_numbers['tuhin'])
# print(favorite_numbers['borna'])
# print(favorite_numbers['tasmia'])

for name, numbers in favorite_numbers.items():
    print(f"{name} favorite numbers:")
    for number in numbers:
        print(f"\t{number}")