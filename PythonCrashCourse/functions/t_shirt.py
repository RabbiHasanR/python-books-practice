def make_shirt(size):
    """Display the shirt size"""
    print(f"The t_shirt size is {size}")

make_shirt(23)


def describe_city(city_name, country='Bangladesh'):
    """Describe city information"""
    print(f"{city_name.title()} is in {country.title()}")

describe_city('Dhaka')
describe_city(city_name='london', country='England')
describe_city(country='USA', city_name='new york')
describe_city('tokyo', 'japan')