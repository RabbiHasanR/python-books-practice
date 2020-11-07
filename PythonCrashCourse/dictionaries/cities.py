cities = {
    'dhaka': {'country': 'Bangladesh', 'population': 1234567890, 'fact': 'capital'},
    'london': {'country': 'England', 'population': 1234567890, 'fact': 'capital'},
    'new york': {'country': 'USA', 'population': 1234567890, 'fact': 'capital'},
}

for city, info in cities.items():
    print(f"{city.title()} information:")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")