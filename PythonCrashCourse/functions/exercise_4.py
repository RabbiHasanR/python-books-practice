def make_sandwiches(*sandwiches):
    """Summarize the sandwiches we are about to make."""
    print(f"\nSandwiches with the following toppings:")
    for sandwiche in sandwiches:
        print(f"- {sandwiche}")

make_sandwiches('pepperoni')
make_sandwiches('mushrooms', 'green peppers', 'extra cheese')

def make_car(manufacturer, model_name, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)