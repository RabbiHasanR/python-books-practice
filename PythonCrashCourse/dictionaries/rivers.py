rivers = {
    'nile': 'egypt',
    'temps': 'london',
    'padha': 'bangladesh'
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)